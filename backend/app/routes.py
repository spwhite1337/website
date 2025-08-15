from flask import jsonify, request

from apis.process_gambling.process_gambling import bets


from app import app


@app.route('/api/processgambling', methods=['GET', 'POST'])
def sports_bettors():
    if request.method == 'GET':
        # inputs=request.args
        output = bet()
    else:
        output = 'blank'
    return jsonify({'output': output})


@app.route('/', defaults={'path': ''})
@app.route('/<path:path>')
def catch_all(path):
    message = 'Greetings from the Backend'
    message += ' ({})'.format(path) if path else ''
    return jsonify({'message': message})

