Certainly! Below is the `pytest` script for testing a Flask API defined in `app.py` with a `/hello` endpoint that returns `'Hello, World!'` as JSON. I've included a pytest fixture to create a test client and a test function to check if the endpoint returns the correct status code and JSON.

First, ensure your `app.py` looks like this:

```python
from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/hello', methods=['GET'])
def hello():
    return jsonify({'message': 'Hello, World!'})

if __name__ == '__main__':
    app.run(debug=True)
```

Now, create a `test_app.py` file with the following content:

```python
import pytest
from app import app

@pytest.fixture
def client():
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client

def test_hello_endpoint(client):
    response = client.get('/hello')
    assert response.status_code == 200
    assert response.json == {'message': 'Hello, World!'}
```

To run the tests, make sure you have `pytest` installed (`pip install pytest`) and then execute the following command in your terminal:

```sh
pytest test_app.py
```

This will run the test and verify that the `/hello` endpoint returns a status code of 200 and the correct JSON response.