# app.py
from flask import Flask, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route('/api/items', methods=['GET'])
def get_items():
    items = [
        {"id": 1, "name": "banana"},
        {"id": 2, "name": "strawberry"},
        {"id": 3, "name": "apple"}
    ]
    return jsonify(items)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5120)