```python
import pytest
from flask import Flask

# Assuming your app is in a file named app.py
from app import app

@pytest.fixture
def client():
    with app.test_request_context():
        yield app.test_client()

def test_hello_endpoint(client):
    response = client.get('/hello')
    assert response.status_code == 200
    assert response.data == b'Hello, World!'
```