import os
import boto3
import uuid
from time import gmtime, strftime
from dateutil.parser import *
from flask import Flask, jsonify, request, make_response, json
from flask_cors import CORS

app = Flask(__name__)
CORS(app, resources={r"/*": {"origins": "https://quarantinenotes.com"}})

NOTES_TABLE = os.environ['NOTES_TABLE']
IS_OFFLINE = os.environ.get('IS_OFFLINE')
RESPONSE_HEADERS =  {
    'Access-Control-Allow-Origin': 'https://quarantinenotes.com',
    'Access-Control-Allow-Headers': '*',
    'Access-Control-Allow-Credentials': 'true',
    'Content-Type': 'application/json'
}

if IS_OFFLINE:
    client = boto3.client(
        'dynamodb',
        region_name='localhost',
        endpoint_url='http://localhost:8000'
    )
else:
    client = boto3.client('dynamodb')


@app.route("/", methods=["GET"])
def list_notes():
    country = request.args.get('country')
    if country:
        response = client.scan(
            TableName=NOTES_TABLE,
            ScanFilter={
                'country': {
                    'AttributeValueList': [{ 'S': country}],
                    'ComparisonOperator': 'EQ'
                }
            }
        )
    else:
        response = client.scan(TableName=NOTES_TABLE)

    notes = []
    for item in response.get('Items'):
        notes.append({
            'noteId': item.get('noteId').get('S'),
            'content': item.get('content').get('S'),
            'author': item.get('author').get('S'),
            'country': item.get('country').get('S'),
            'replies': format_note_replies(item.get('replies')),
            'createdAt': item.get('createdAt').get('S')
        })
    notes = sorted(notes, key=lambda note: parse(note['createdAt']), reverse=True)

    return make_response(jsonify(notes), 200, RESPONSE_HEADERS)


@app.route("/notes/<string:note_id>", methods=["GET"])
def get_note(note_id):
    resp = client.get_item(
        TableName=NOTES_TABLE,
        Key={
            'noteId': { 'S': note_id }
        }
    )
    item = resp.get('Item')
    if not item:
        return jsonify({'error': 'Note does not exist'}), 404

    return make_response(
        jsonify({
            'noteId': item.get('noteId').get('S'),
            'content': item.get('content').get('S'),
            'author': item.get('author').get('S'),
            'country': item.get('country').get('S'),
            'createdAt': item.get('createdAt').get('S')
        }),
        200,
        RESPONSE_HEADERS
    )


@app.route("/notes", methods=["POST"])
def create_note():
    content = request.json.get('content')
    author = request.json.get('author') or 'Anonymous'
    country = request.json.get('country') or 'Unknown'
    note_id = uuid.uuid4().hex
    created_at = strftime("%a, %d %b %Y %H:%M:%S +0000", gmtime())
    if not note_id or not content:
        return jsonify({'error': 'Please provide noteId and content'}), 400

    resp = client.put_item(
        TableName=NOTES_TABLE,
        Item={
            'noteId': {'S': note_id },
            'content': {'S': content },
            'author': {'S': author },
            'country': {'S': country },
            'createdAt': {'S': created_at }
        }
    )
    json_note = jsonify({
        'noteId': note_id,
        'content': content,
        'author': author,
        'country': country,
        'createdAt': created_at
    })
    print(">> ADDING NOTE")
    print(json_note.data)
    return make_response(
        json_note,
        200,
        RESPONSE_HEADERS
    )

@app.route("/notes/<string:note_id>", methods=["DELETE"])
def delete_note(note_id):
    if(request.args.get('pwd') != os.environ['PWD']):
        return make_response(jsonify({'Error': 'Unauthorized'}), 401, RESPONSE_HEADERS)

    resp = client.delete_item(
        TableName=NOTES_TABLE,
        Key={
            'noteId': { 'S': note_id }
        },
        ReturnValues='ALL_OLD'
    )

    return make_response(jsonify(resp), 200, RESPONSE_HEADERS)

@app.route("/notes/<string:note_id>", methods=["PUT"])
def update_note(note_id):
    reply = request.json.get('reply')

    reply_dynamo_store = {
        'noteId': {'S': uuid.uuid4().hex },
        'content': {'S': reply['content'] },
        'author': {'S': reply['author'] or 'Anonymous' },
        'country': {'S': reply['country'] or 'Unknown' },
        'createdAt': {'S': strftime("%a, %d %b %Y %H:%M:%S +0000", gmtime()) }
    }

    resp = client.update_item(
        TableName=NOTES_TABLE,
        Key={
            'noteId': { 'S': note_id }
        },
        UpdateExpression="SET #attrName = list_append(if_not_exists(#attrName, :empty_list), :r)",
        ExpressionAttributeNames={
            "#attrName": "replies"
        },
        ExpressionAttributeValues={
            ":r": {
                "L": [{
                    'M': reply_dynamo_store
                }]
            },
            ":empty_list": { "L": [] }
        },
        ReturnValues='ALL_NEW'
    )
    json_reply = jsonify(format_response(resp)['replies'].pop())
    print(">> ADDING REPLY TO NOTE " + note_id)
    print(json_reply.data)

    return make_response(json_reply, 200, RESPONSE_HEADERS)

def format_note_replies(notes):
    if notes is None:
        return []

    formatted_notes = []
    notes = notes.get('L')

    for note in notes:
        formatted_note = {
            'author': note.get('M').get('author').get('S'),
            'content': note.get('M').get('content').get('S'),
            'country': note.get('M').get('country').get('S'),
            'createdAt': note.get('M').get('createdAt').get('S'),
            'noteId': note.get('M').get('noteId').get('S')
        }
        formatted_notes.append(formatted_note)

    return formatted_notes

def format_response(data):
    return {
        'author': data.get('Attributes').get('author').get('S'),
        'content': data.get('Attributes').get('content').get('S'),
        'country': data.get('Attributes').get('country').get('S'),
        'createdAt': data.get('Attributes').get('createdAt').get('S'),
        'noteId': data.get('Attributes').get('noteId').get('S'),
        'replies': format_note_replies(data.get('Attributes').get('replies'))
    }
