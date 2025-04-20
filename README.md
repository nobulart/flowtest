```markdown
# Flask API

A simple Flask API with a /hello endpoint that returns 'Hello, World!' as JSON.

## Installation

1. Install Python 3.9+
2. Create a virtual environment (optional but recommended):
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```
3. Install dependencies:
   ```bash
   pip install flask
   ```

## Running

1. Run the app:
   ```bash
   python app.py
   ```
2. Access the endpoint:
   ```bash
   curl http://localhost:5000/hello
   ```
   You should receive a JSON response:
   ```json
   {"message": "Hello, World!"}
   ```

## Example Code

Here is an example of what your `app.py` might look like:

```python
from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/hello', methods=['GET'])
def hello():
    return jsonify(message="Hello, World!")

if __name__ == '__main__':
    app.run(debug=True)
```
```