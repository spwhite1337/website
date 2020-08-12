from flask import jsonify, render_template, flash, redirect, url_for, request
from flask_login import login_user, logout_user, current_user, login_required
from werkzeug.urls import url_parse

from app import app, db
from app.forms import LoginForm, RegistrationForm
from app.models import User, Comment

from apis.presidents_speeches import ps_api
from apis.sports_bettors import sb_api
from apis.card_classifier import cc_api
from sports_bettors.dash import add_sb_dash


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


# Login Routes
@app.route('/api/index')
@login_required
def index():
    return render_template('index.html', title='Home')


@app.route('/api/login', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('index'))
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data).first()
        if user is None or not user.check_password(form.password.data):
            flash('Invalid username or password')
            return redirect(url_for('login'))
        login_user(user, remember=form.remember_me.data)
        next_page = request.args.get('next')
        if not next_page or url_parse(next_page).netloc != '':
            next_page = url_for('index')
        return redirect(next_page)
    return render_template('login.html', title='Sign In', form=form)


@app.route('/api/logout')
def logout():
    logout_user()
    return redirect(url_for('index'))


@app.route('/api/register', methods=['GET', 'POST'])
def register():
    if current_user.is_authenticated:
        return redirect(url_for('index'))
    form = RegistrationForm()
    if form.validate_on_submit():
        user = User(username=form.username.data, email=form.email.data)
        user.set_password(form.password.data)
        db.session.add(user)
        db.session.commit()
        flash('Congratulations, you are now a registered user!')
        return redirect(url_for('login'))
    return render_template('register.html', title='Register', form=form)


@app.route('/api/comment', methods=['GET', 'POST'])
def write_comment():
    if not current_user.is_authenticated:
        return jsonify({'message': 'Login to comment'})
    else:
        # Update database
        comment = Comment(post=request.args['post'], comment=request.arg['comment'], user_id=current_user.id)
        db.session.add(comment)
        db.session.commit()

        return jsonify({'message': 'Comment added'})


@app.route('/', defaults={'path': ''})
@app.route('/<path:path>')
def catch_all(path):
    message = 'Greetings from the Backend'
    message += ' ({})'.format(path) if path else ''
    return jsonify({'message': message})
