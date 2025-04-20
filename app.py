Certainly! Below is a Python script for a Flask REST API with a single `/hello` endpoint that returns "Hello, World!" as a JSON response using Flask's `jsonify`.

```python
from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/hello', methods=['GET'])
def hello():
    return jsonify({'message': 'Hello, World!'})

if __name__ == '__main__':
    app.run(debug=True)
```

### Explanation:

1. **Importing Flask and jsonify:**
   - `Flask` is the main class for creating a Flask application.
   - `jsonify` is a helper function to create JSON responses.

2. **Creating the Flask App:**
   - `app = Flask(__name__)` initializes a new Flask application instance.

3. **Defining the `/hello` Endpoint:**
   - `@app.route('/hello', methods=['GET'])` defines a route for the `/hello` endpoint that accepts GET requests.
   - The function `hello()` returns a JSON response using `jsonify({'message': 'Hello, World!'})`.

4. **Running the App:**
   - `if __name__ == '__main__':` ensures that the app runs only if the script is executed directly (not imported as a module).
   - `app.run(debug=True)` starts the Flask development server with debugging enabled.

### Running the Application

1. Save the script to a file, e.g., `app.py`.
2. Run the application using the command:

    ```bash
    python app.py
    ```

3. Access the `/hello` endpoint by navigating to `http://localhost:5000/hello` in your web browser or using a tool like `curl` or Postman.

    ```bash
    curl http://localhost:5000/hello
    ```

This will return the JSON response:

```json
{
  "message": "Hello, World!"
}
```

### Example Directory Structure

Assuming you have saved the script in a directory named `flask_hello_world`:

```
flask_hello_world/
│
├── app.py
└── README.md
```

This setup allows you to easily manage and run your Flask application.