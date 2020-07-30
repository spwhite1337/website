from flask import Flask, request


app = Flask(__name__, static_folder="../dist/static", template_folder="../dist")


@app.route('/api/test', methods=['GET'])
def test():
    if request.method == 'GET':
        return {'test': 'Hi from flask (test)'}


@app.route('/', defaults={'path': ''})
@app.route('/<path:path>')
def catch_all(path):
    return "Hi from Flask"


if __name__ == '__main__':
    app.run(host='0.0.0.0')
