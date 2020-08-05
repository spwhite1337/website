from werkzeug.middleware.dispatcher import DispatcherMiddleware

from run import app
from apis.dash.sports_bettors import dashapp as sb_app

app.wsgi_app = DispatcherMiddleware(app.wsgi_app, {'/api/dash/': sb_app.server})

if __name__ == "__main__":
    app.run(host='127.0.0.1', port=5000)
