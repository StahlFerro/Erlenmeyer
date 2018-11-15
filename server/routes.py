import string
from random import choices
from pprint import pprint
from server import app
from flask import request, render_template, redirect, jsonify, flash, url_for, abort
from flask_login import current_user, login_user, logout_user, login_required, AnonymousUserMixin
from werkzeug.urls import url_parse
from server.forms import LoginForm
from server.models import User


def get_data(id: int = None):
    count = 100
    charlength = 20
    numlength = 25
    data = [{
        'id': x,
        'name': "".join(choices(string.ascii_letters, k=charlength)),
        'number': "".join(choices(string.digits, k=numlength))
    } for x in range(0, count)]
    if not id:
        return data
    else:
        return [d for d in data if d['id'] == id]


@app.route('/', methods=['GET', 'POST'])
@app.route('/index', methods=['GET', 'POST'])
def index():
    print('index called')
    username = ''
    is_login = current_user.is_authenticated
    if is_login:
        username = current_user.username
    return render_template('index.html', username=username, is_login=is_login)


@app.route('/index/ships', methods=['GET', 'POST'])
def ships():
    return render_template('ships.html')


@app.route('/gate', methods=['GET', 'POST'])
def login():
    print('gate called')
    if current_user.is_authenticated:
        return redirect(url_for('login'))
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data).first()
        print(f'Login user {user}')
        if user is None or not user.check_password(form.password.data): # If user does not exist or has wrong username and pass
            flash('Invalid username or password')
            return redirect(url_for('login'))
        else:  # If user exist and has the correct username and pass
            login_user(user, remember=form.remember_me.data)
            next_page = request.args.get('next')
            if not next_page or url_parse(next_page).netloc != '':
                next_page = url_for('index')
            print(f'next page: {next_page}')
            return redirect(next_page)
    return render_template('gate.html', title='Login', form=form)


@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('index'))