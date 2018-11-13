import string
from random import choices
from pprint import pprint
from server import app
from flask import render_template, redirect, jsonify, flash, url_for, abort
from flask_login import current_user, login_user, logout_user, AnonymousUserMixin
from server.forms import LoginForm
from server.models import User


def get_data():
    count = 10
    charlength = 20
    numlength = 25
    data = [{
        'id': x,
        'name': "".join(choices(string.ascii_letters, k=charlength)),
        'number': "".join(choices(string.digits, k=numlength))
    } for x in range(0, count)]
    return data


@app.route('/')
@app.route('/index')
def index():
    user = current_user
    is_login = current_user.is_authenticated
    if user.is_anonymous:
        username = 'guest'
    else:
        username = user.username
    data = get_data()
    return render_template('index.html', title='IMVR', username=username, data=data, is_login=is_login)


@app.route('/json', methods=['GET'])
def jsonall():
    return jsonify(get_data())


@app.route('/json/<int:urlid>', methods=['GET'])
def json(urlid=None):
    record = [data for data in get_data() if data['id'] == urlid]
    if len(record) == 0:
        abort(404)
    return jsonify(record)


@app.route('/login', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('index'))
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data).first()
        print(f'Login user {user}')
        if user is None or not user.check_password(form.password.data):
            flash('Invalid username or password')
            return redirect(url_for('login'))
        login_user(user, remember=form.remember_me.data)
        return redirect(url_for('index'))
    return render_template('login.html', title='Login', form=form)


@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('index'))
