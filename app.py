import os
import boto3
import uuid
from time import gmtime, strftime
from flask import Flask, jsonify, request, make_response
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
            'createdAt': item.get('createdAt').get('S')
        })
    notes = sorted(notes, key=lambda note: note['createdAt'], reverse=True)

    return make_response(jsonify(notes), 200, RESPONSE_HEADERS)


@app.route("/notes/<string:note_id>")
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

    return make_response(
        jsonify({
            'noteId': note_id,
            'content': content,
            'author': author,
            'country': country,
            'createdAt': created_at
        }),
        200,
        RESPONSE_HEADERS
    )
