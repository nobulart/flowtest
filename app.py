from flask import Flask, jsonify
import pandas as pd
from pathlib import Path
app = Flask(__name__)


@app.route('/hello')
def hello():
    return jsonify({'message': 'Hello, World!'})


@app.route('/data')
def data():
    if Path('data.csv').exists():
        df = pd.read_csv('data.csv')
        return jsonify(df.head().to_dict())
    return jsonify({'error': 'Dataset not found'})


if __name__ == '__main__':
    app.run()