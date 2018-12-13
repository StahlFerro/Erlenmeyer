from werkzeug.urls import url_parse
from flask_login import current_user, login_user, logout_user
from flask import request, render_template, redirect, jsonify, flash, url_for, abort

from server import app, db, session
from server.models import Ship, ShipType, ShipStatus, Engine, Builder
from server.forms import LoginForm
from server.models import User
from server.utils.orm import format_headers, get_web_columns, get_json_data
from server.utils.url import is_safe_url


@app.route('/', methods=['GET', 'POST'])
@app.route('/index', methods=['GET', 'POST'])
def index():
    print('index called')
    username = ''
    is_login = current_user.is_authenticated
    if is_login:
        username = current_user.username
    return render_template('index.html', username=username, is_login=is_login)


@app.route('/index/ship', methods=['GET', 'POST'])
@app.route('/index/ship/<int:ship_id>')
def ship(ship_id: int=None):
    print('ships called with id:', ship_id or 'none')
    ship_cols = get_web_columns(Ship)
    cap_headers = format_headers(ship_cols)
    ship_data = get_json_data(model=Ship, columns=ship_cols, id=ship_id)
    print('ship data', ship_data)
    return render_template('registry.html', title='Ships', headers=ship_cols, data=ship_data,
                           cap_headers=cap_headers, index=1)


@app.route('/index/ship_type', methods=['GET', 'POST'])
@app.route('/index/ship_type/<int:ship_type_id>')
def ship_type(ship_type_id: int=None):
    print('ship types called with id:', ship_type_id or 'none')
    stype_cols = get_web_columns(ShipType)
    cap_headers = format_headers(stype_cols)
    stype_data = get_json_data(model=ShipType, columns=stype_cols, id=ship_type_id)
    print('ship type data', stype_data)
    return render_template('registry.html', title='Ship Types', headers=stype_cols, data=stype_data,
                           cap_headers=cap_headers, index=1)


@app.route('/index/ship_status', methods=['GET', 'POST'])
@app.route('/index/ship_status/<int:ship_status_id>')
def ship_status(ship_status_id: int=None):
    print('ship types called with id:', ship_status_id or 'none')
    stat_cols = get_web_columns(ShipStatus)
    cap_headers = format_headers(stat_cols)
    stat_data = get_json_data(model=ShipStatus, columns=stat_cols, id=ship_status_id)
    print('ship type data', stat_data)
    return render_template('registry.html', title='Ship Statuses', headers=stat_cols, data=stat_data,
                           cap_headers=cap_headers, index=1)


@app.route('/index/engine', methods=['GET', 'POST'])
@app.route('/index/engine/<int:engine_id>', methods=['GET', 'POST'])
def engine(engine_id: int=None):
    engine_cols = get_web_columns(Engine)
    cap_headers = format_headers(engine_cols)
    engine_data = get_json_data(model=Engine, columns=engine_cols, id=engine_id)
    return render_template('registry.html', title='Engines', headers=engine_cols, data=engine_data,
                           cap_headers=cap_headers, index=1)


@app.route('/index/builder', methods=['GET', 'POST'])
@app.route('/index/builder/<int:builder_id>', methods=['GET', 'POST'])
def builder(builder_id: int=None):
    builder_cols = get_web_columns(Builder)
    cap_headers = format_headers(builder_cols)
    builder_data = get_json_data(model=Builder, columns=builder_cols, id=builder_id)
    return render_template('registry.html', title='Builders', headers=builder_cols, data=builder_data,
                           cap_headers=cap_headers, index=1)


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
            if not is_safe_url(next_page):
                return app.abort(400)
            print(f'next page: {next_page}')
            return redirect(next_page)
    return render_template('gate.html', title='Login', form=form)


@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('index'))


@app.route('/user_profile')
def user_profile():
    return render_template('user_profile.html', user=current_user)


print(__name__)
