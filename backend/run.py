from flask import Flask, request
from flask_cors import CORS


app = Flask(__name__)
cors = CORS(app, resources={r"/api/*": {"origins": "*"}})


@app.route('/api/presidentsspeeches', methods=['GET'])
def presidents_speeches():
    response = {'president': 'none'}
    if request.method == 'GET':
        return {'president': 'Hi from flask (presidents speeches)'}
    return response


@app.route('/api/sportsbettors', methods=['GET'])
def sports_bettors():
    response = {'sb_output': 'none'}
    if request.method == 'GET':
        return {'sb_output': 'Hi from flask (sports bettors)'}
    return response


@app.route('/api/cardclassifier', methods=['GET'])
def card_classifier():
    response = {'card_color': 'none'}
    if request.method == 'GET':
        return {'card_color': 'Hi from flask (card classifier)'}
    return response


@app.route('/', defaults={'path': ''})
@app.route('/<path:path>')
def catch_all(path):
    return {'test': "Hi from Flask"}


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
