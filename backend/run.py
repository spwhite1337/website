from flask import Flask, jsonify, request
from flask_cors import CORS

from apis.presidents_speeches import ps_api
from apis.sports_bettors import sb_api
from apis.card_classifier import cc_api

from sports_bettors.dash import add_sb_dash

app = Flask(__name__)
cors = CORS(app, resources={r"/api/*": {"origins": "*"}})


# Add Dash apps
# Nice tutorial on Flask + Dash integration: https://hackersandslackers.com/plotly-dash-with-flask/
app = add_sb_dash(app, routes_pathname_prefix='/api/dash/sportsbettors/')


@app.route('/api/sportsbettors', methods=['GET', 'POST'])
def sports_bettors():
    # response = jsonify({'sb_output': 'blank'})
    if request.method == 'GET':
        # if 'league' in request.args.keys():
        #     response = sb_api(request.args)
        #     return jsonify({'sb_output': response})
        output = sb_api(inputs=request.args) if 'league' in request.keys() else 'blank'
    else:
        output = 'blank'
    return jsonify({'sb_output': output})


@app.route('/api/cardclassifier', methods=['GET', 'POST'])
def card_classifier():
    if request.method == 'GET':
        # if 'default_card' in request.args.keys():
            # output = cc_api(default_card=request.args['default_card'])
            # return jsonify({'card_color': output})
        output = cc_api(default_card=request.args['default_card']) if 'default_card' in request.args.keys() else 'blank'
    else:
        output = 'blank'
    return jsonify({'card_color': output})


@app.route('/api/presidentsspeeches', methods=['GET', 'POST'])
def presidents_speeches():
    if request.method == 'GET':
        # if 'query' in request.args.keys():
        #     output = ps_api(request.args['query'])
        #     return jsonify({'president': output})
        output = ps_api(query=request.args['query']) if 'query' in request.args.keys() else 'blank'
    else:
        output = 'blank'
    return jsonify({'president': output})


@app.route('/', defaults={'path': ''})
@app.route('/<path:path>')
def catch_all(path):
    return jsonify({'message': 'Greetings from the Backend'})


if __name__ == '__main__':
    app.run(host='127.0.0.1', port=5000)
