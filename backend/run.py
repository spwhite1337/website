import requests
from flask import Flask, render_template, jsonify, request
from flask_cors import CORS

from backend.apis.presidents_speeches import ps_api
from backend.apis.sports_bettors import sb_api
from backend.apis.card_classifier import cc_api

from config import logger


app = Flask(__name__, static_folder="../dist/static", template_folder="../dist")
cors = CORS(app, resources={r"/api/*": {"origins": "*"}})


@app.route('/api/sportsbettors', methods=['GET', 'POST'])
def sports_bettors():
    args = request.args
    logger.info(args)
    response = {'sb_output': 'got em'}
    return jsonify(response)


@app.route('/api/cardclassifier', methods=['GET', 'POST'])
def card_classifier():
    args = request.args
    response = {'card_color': ''}
    if 'default_card' in args.keys():
        output = cc_api(default_card=args['default_card'])
        response = {'card_color': output}
    return jsonify(response)


@app.route('/api/presidentsspeeches', methods=['GET', 'POST'])
def presidents_speeches():
    args = request.args
    if 'query' in args.keys():
        response = {'president': ps_api(args['query'])}
    else:
        response = {'president': 'Scott'}
    return jsonify(response)


@app.route('/', defaults={'path': ''})
@app.route('/<path:path>')
def catch_all(path):
    if app.debug:
        return requests.get('http://localhost:8080/{}'.format(path)).text
    return render_template("index.html")
