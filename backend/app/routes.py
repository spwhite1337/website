from flask import jsonify, request

from apis.utils.process_gambling.process_gambling import bets
from apis.utils.job_search.job_search import add_js_dash


from app import app


@app.route('/api/processgambling', methods=['GET', 'POST'])
def sports_bettors():
    if request.method == 'GET':
        # inputs=request.args
        output = bet()
    else:
        output = 'blank'
    return jsonify({'output': output})


# Add dashboard for job-search
app = add_js_dash(app, routes_pathname_prefix='/api/dash/jobsearch/')


@app.route('/', defaults={'path': ''})
@app.route('/<path:path>')
def catch_all(path):
    message = 'Greetings from the Backend'
    message += ' ({})'.format(path) if path else ''
    return jsonify({'message': message})

