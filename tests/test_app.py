```python
import pytest
from flask import Flask

# Import your app (assuming it's in a file named 'app.py')
from app import app  # Replace 'app' with the actual name of your Flask app instance


@pytest.fixture
def client():
    """Create a test client for the Flask app."""
    with app.test_request_context():
        yield app.test_client()


def test_hello_endpoint(client):
    """Test that the /hello endpoint returns 'Hello, World!'."""
    response = client.get('/hello')
    assert response.status_code == 200
    assert response.data == b'Hello, World!'  # Compare as bytes


if __name__ == '__main__':
    pytest.main()
```

**Explanation:**

1. **Import necessary modules:** `pytest` for testing and `Flask` to interact with the Flask app.
2. **Import your Flask app:** The line `from app import app` imports your Flask application instance from its file (e.g., if your Flask app is defined in a file named `app.py`, you would import it like this).  **Make sure to replace `"app"` with the actual name of your Flask app instance.**
3. **Create a test client fixture:**
   - `@pytest.fixture` decorator defines a function that provides a reusable resource for tests. In this case, it creates a `test_client` which is a convenient way to make requests to your Flask app during testing without actually running the server.
   - `with app.test_request_context():` sets up the Flask application context for testing. This is essential because some Flask features rely on being within an application context.
   - `yield app.test_client()` provides the test client to the tests that use this fixture.  The `yield` keyword makes it a generator, ensuring proper cleanup after each test.
4. **Define a test function:**
   - `def test_hello_endpoint(client):` defines a test function named `test_hello_endpoint`. It takes the `client` fixture as an argument.
   - `response = client.get('/hello')`:  Makes a GET request to the `/hello` endpoint using the test client.
   - `assert response.status_code == 200`: Checks that the HTTP status code is 200 (OK).
   - `assert response.data == b'Hello, World!'`: Checks that the response data matches the expected value ("Hello, World!").  Note that we compare it as bytes (`b'...'`) because `response.data` returns a byte string.

**How to run the tests:**

1. **Save the test script:** Save this code in a file named `test_app.py` (or any other name you prefer) in the same directory as your Flask application file (`app.py`).
2. **Install pytest:** If you don't have pytest installed, run `pip install pytest`.
3. **Run the tests:** Open your terminal and navigate to the directory containing the test script and Flask app. Then run the command `pytest`.

Pytest will automatically discover and run all functions that start with `test_` in your test files.  It will then report whether each test passed or failed.