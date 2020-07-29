from flask import Flask, render_template, jsonify, request
from flask_cors import CORS


app = Flask(__name__, static_folder="../dist/static", template_folder="../dist")
cors = CORS(app, resources={r"/api/*": {"origins": "*"}})


@app.route('/api/sportsbettors', methods=['GET', 'POST'])
def sports_bettors():
    if request.method == 'GET':
        return jsonify({'sb_output': 'output'})

    else:
        return jsonify({})


@app.route('/api/cardclassifier', methods=['GET', 'POST'])
def card_classifier():
    if request.method == 'GET':
        return jsonify({'card_color': 'output'})

    else:
        return jsonify({})


@app.route('/api/presidentsspeeches', methods=['GET', 'POST'])
def presidents_speeches():
    if request.method == 'GET':
        return jsonify({'president': 'output'})

    else:
        return jsonify({})


@app.route('/', defaults={'path': ''})
@app.route('/<path:path>')
def catch_all(path):
    return "Hi from Flask"


if __name__ == '__main__':
    app.run(host='0.0.0.0')
