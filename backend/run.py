from flask import Flask, request
from flask_cors import CORS


app = Flask(__name__, static_folder="../dist/static", template_folder="../dist")
cors = CORS(app, resources={r"/api/*": {"origins": "*"}})


@app.route('/api/presidentsspeeches', methods=['GET'])
def presidents_speeches():
    response = {'test': 'none'}
    if request.method == 'GET':
        return {'test': 'Hi from flask (presidents speeches)'}
    return response


@app.route('/api/sportsbettors', methods=['GET'])
def sports_bettors():
    response = {'test': 'none'}
    if request.method == 'GET':
        return {'test': 'Hi from flask (sports bettors)'}
    return response


@app.route('/api/cardclassifier', methods=['GET'])
def card_classifier():
    response = {'test': 'none'}
    if request.method == 'GET':
        return {'test': 'Hi from flask (card classifier)'}
    return response


@app.route('/', defaults={'path': ''})
@app.route('/<path:path>')
def catch_all(path):
    return {'test': "Hi from Flask"}


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
