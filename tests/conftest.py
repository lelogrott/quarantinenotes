import os

os.environ['IS_OFFLINE'] = '1'
os.environ['NOTES_TABLE'] = 'notes-table-test'
os.environ['PWD'] = 'password'

from app import app
import pytest

@pytest.fixture
def client():
    with app.test_client() as client:
        yield client


