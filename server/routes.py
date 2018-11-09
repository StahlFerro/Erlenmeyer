import string
from random import choices
from pprint import pprint
from server import app
from flask import render_template, redirect, jsonify, flash
from server.forms import LoginForm


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
    user = {'name': 'StahlFerro'}
    app_usefulness = 'shit'
    data = get_data()
    return render_template('index.html', title='Erlenmeyer', user=user, data=data, app_usefulness=app_usefulness)


@app.route('/json')
def json():
    return jsonify(get_data())


@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        flash(f'Login requested for user {form.username.data}, remember_me={form.remember_me.data}')
        print(f'Login requested for user {form.username.data}, remember_me={form.remember_me.data}')
        return redirect('/index')
    return render_template('login.html', title='Login', form=form)
