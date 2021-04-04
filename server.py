import json
from flask import Flask, request
from flask_cors import CORS, cross_origin
from api_emotion_compute import *
app = Flask(__name__)
cors = CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'


@app.route('/api/emotion', methods=['POST'])
@cross_origin()
def handle_generate_team():
    body_data = request.get_json()
    print(body_data)
    emotion_result = compute_emotion(body_data)
    return emotion_result


if __name__ == '__main__':
    app.run(port=5050, debug=True)
