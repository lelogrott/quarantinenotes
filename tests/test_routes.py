import os 
import pytest
import json


def test_getting_a_note(client):
    data = dict(
        content='this is a note!',
        author='Joseph Klimber',
        country='Brazil'
    )

    resp = client.post('/notes', json=data)
    assert resp.status_code == 201

    resp = client.get(f"/notes/{resp.json['noteId']}")
    assert resp.status_code == 200
    assert resp.json['content'] == data['content']


def test_creating_a_reply_to_a_note(client):
    data = dict(
        content='this is a note!',
        author='Joseph Klimber',
        country='Brazil'
    )

    resp = client.post('/notes', json=data)
    assert resp.status_code == 201

    reply_data = dict(reply=data)

    resp = client.put(f"/notes/{resp.json['noteId']}", json=reply_data)
    assert resp.status_code == 200


def test_deleting_a_note(client):
    data = dict(
        content='this is a note!',
        author='Joseph Klimber',
        country='Brazil'
    )

    resp = client.post('/notes', json=data)
    assert resp.status_code == 201
    password = os.environ['PWD']
    url = f"/notes/{resp.json['noteId']}?pwd={password}"

    resp = client.delete(url)
    assert resp.status_code == 200


def test_listing_all_notes(client):
    resp = client.get('/')
    assert type(resp.json) is list
    assert resp.status_code == 200