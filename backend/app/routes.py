from flask import jsonify, request

from apis.utils.presidents_speeches.presidents_speeches import ps_api
from apis.utils.sports_bettors.sports_bettors import sb_api
from apis.utils.card_classifier.card_classifier import cc_api
from sports_bettors.dash import add_sb_dash
from apis.utils.job_search.job_search import add_js_dash

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
        output = cc_api(default_card=request.args['selection']) if 'selection' in request.args.keys() else 'blank'
    else:
        output = 'blank'
    return jsonify({'card_color': output})


@app.route('/api/presidentsspeeches', methods=['GET', 'POST'])
def presidents_speeches():
    if request.method == 'GET':
        output = ps_api(query=request.args['query']) if 'query' in request.args.keys() else 'blank'
    else:
        output = {'presidents': ['blank'], 'presidents_sim': [1.0], 'speeches': ['blank'], 'speeches_sim': [1.0]}
    return jsonify(output)


# Add dashboard for job-search
app = add_js_dash(app, routes_pathname_prefix='/api/dash/jobsearch/')


@app.route('/', defaults={'path': ''})
@app.route('/<path:path>')
def catch_all(path):
    message = 'Greetings from the Backend'
    message += ' ({})'.format(path) if path else ''
    return jsonify({'message': message})
