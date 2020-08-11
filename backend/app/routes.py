from flask import jsonify, request

from apis.presidents_speeches import ps_api
from apis.sports_bettors import sb_api
from apis.card_classifier import cc_api
from sports_bettors.dash import add_sb_dash

from app import app


@app.route('/api/sportsbettors', methods=['GET', 'POST'])
def sports_bettors():
    if request.method == 'GET':
        output = sb_api(inputs=request.args) if 'league' in request.args.keys() else 'blank'
    else:
        output = 'blank'
    return jsonify({'sb_output': output})


# Add Dash app
# Nice tutorial on Flask + Dash integration: https://hackersandslackers.com/plotly-dash-with-flask/
app = add_sb_dash(app, routes_pathname_prefix='/api/dash/sportsbettors/')


@app.route('/api/cardclassifier', methods=['GET', 'POST'])
def card_classifier():
    if request.method == 'GET':
        output = cc_api(default_card=request.args['default_card']) if 'default_card' in request.args.keys() else 'blank'
    else:
        output = 'blank'
    return jsonify({'card_color': output})


@app.route('/api/presidentsspeeches', methods=['GET', 'POST'])
def presidents_speeches():
    if request.method == 'GET':
        output = ps_api(query=request.args['query']) if 'query' in request.args.keys() else 'blank'
    else:
        output = 'blank'
    return jsonify({'president': output})


@app.route('/', defaults={'path': ''})
@app.route('/<path:path>')
def catch_all(path):
    message = 'Greetings from the Backend'
    message += ' ({})'.format(path) if path else ''
    return jsonify({'message': message})
