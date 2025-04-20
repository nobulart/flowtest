Certainly! Here is the Python script for a Flask REST API with a single `/hello` endpoint that returns `'Hello, World!'` as JSON:

```python
from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/hello', methods=['GET'])
def hello():
    return jsonify({'message': 'Hello, World!'})

if __name__ == '__main__':
    app.run()
```

To run this script:
1. Ensure you have Flask installed (`pip install flask`).
2. Save the code to a file, e.g., `app.py`.
3. Run the application using `python app.py`.
4. Access the `/hello` endpoint via your web browser or tools like curl at `http://localhost:5000/hello`.

This will return `{"message": "Hello, World!"}` in JSON format in response to GET requests at the `/hello` endpoint.