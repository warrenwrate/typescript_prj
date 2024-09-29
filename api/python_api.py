# app.py
from flask import Flask, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route('/api/items', methods=['GET'])
def get_items():
    items = [
        {"id": 1, "name": "Item 1"},
        {"id": 2, "name": "Item 2"},
        {"id": 3, "name": "Item 3"}
    ]
    return jsonify(items)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5120)