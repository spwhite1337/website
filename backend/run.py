import requests
from flask import Flask, render_template, jsonify, request
from flask_cors import CORS

from backend.apis.presidents_speeches import ps_api
from backend.apis.sports_bettors import sb_api
from backend.apis.card_classifier import cc_api


app = Flask(__name__, static_folder="../dist/static", template_folder="../dist")
cors = CORS(app, resources={r"/api/*": {"origins": "*"}})


@app.route('/api/sportsbettors', methods=['GET', 'POST'])
def sports_bettors():
    if request.method == 'GET':
        response = sb_api(request.args)
        return jsonify({'sb_output': response})

    else:
        return jsonify({})


@app.route('/api/cardclassifier', methods=['GET', 'POST'])
def card_classifier():
    if request.method == 'GET':
        output = cc_api(default_card=request.args['default_card'])
        return jsonify({'card_color': output})

    else:
        return jsonify({})


@app.route('/api/presidentsspeeches', methods=['GET', 'POST'])
def presidents_speeches():
    if request.method == 'GET':
        output = ps_api(request.args['query'])
        return jsonify({'president': output})

    else:
        return jsonify({})


@app.route('/', defaults={'path': ''})
@app.route('/<path:path>')
def catch_all(path):
    if app.debug:
        return requests.get('http://localhost:8080/{}'.format(path)).text
    return render_template("index.html")


if __name__ == '__main__':
    app.run(host='0.0.0.0')
