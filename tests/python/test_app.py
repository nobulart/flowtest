from flask import Flask
import pytest
from pathlib import Path
from ..app import app


@pytest.fixture
def client():
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client


def test_hello_endpoint(client):
    response = client.get('/hello')
    assert response.status_code == 200
    assert response.json == {'message': 'Hello, World!'}


def test_data_endpoint(client):
    response = client.get('/data')
    assert response.status_code == 200
    if Path('data.csv').exists():
        assert isinstance(response.json, dict)
    else:
        assert response.json == {'error': 'Dataset not found'}