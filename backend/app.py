from flask import Flask, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route('/')
def hello_world():
    return 'Hello, World! This is a Flask app running in Docker.'

@app.route('/api/message', methods=['GET'])
def get_message():
    return jsonify({'message': 'Hello from Flask!'})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5050)
