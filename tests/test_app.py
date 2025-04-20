```python
import pytest
from flask import Flask
from app import app  # Assuming your app is in app.py
import json

@pytest.fixture
def client():
    with app.test_request_context():
        yield app.test_client()

def test_hello_endpoint(client):
    response = client.get('/hello')
    assert response.status_code == 200
    data = response.get_json()  # Get the JSON data from the response
    assert data['message'] == 'Hello, World!'
```