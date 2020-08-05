from run import app
from apis.dash.sports_bettors import add_sb_dash
from apis.dash.card_classifier import add_cc_dash


# Nice tutorial on Flask + Dash integration:
# https://hackersandslackers.com/plotly-dash-with-flask/

# Add Sports-Bettors Dash Board to Flask Server
app = add_sb_dash(app, routes_pathname_prefix='/api/dash/sportsbettors/')

# Add Card Classifier Dash Board to Flask Server (as an example of multiple dash boards)
app = add_cc_dash(app, routes_pathname_prefix='/api/dash/cardclassifier/')

if __name__ == "__main__":
    app.run(host='127.0.0.1', port=5000)
