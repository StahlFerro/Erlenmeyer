from werkzeug.urls import url_parse
from flask_login import current_user, login_user, logout_user
from flask import request, render_template, redirect, jsonify, flash, url_for, abort

from server import app, db, session
from server.models import Ship, ShipType, ShipStatus, Engine, Builder
from server.forms import LoginForm, ShipForm, ShipTypeForm, ShipStatusForm, EngineForm, BuilderForm
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
@app.route('/index/ship/<int:rec_id>')
def ship_view(rec_id: int = None):
    model = Ship
    print('ships called with id:', rec_id or 'none')
    ship_cols = get_web_columns(model)
    cap_headers = format_headers(ship_cols)
    ship_data = get_json_data(model=model, columns=ship_cols, id=rec_id)
    print('ship data', ship_data)
    authenticated = current_user.is_authenticated
    return render_template('registry.html', title='Ships', headers=ship_cols, data=ship_data,
                           cap_headers=cap_headers, authenticated=authenticated, model_name='ship')


@app.route('/index/ship/create', methods=['GET', 'POST'])
def ship_create():
    form = ShipForm()
    print(form.__dict__)
    if form.validate_on_submit():
        ship = Ship()
        form.populate_obj(ship)
        print(ship, ship.code)
    return render_template('multiform.html', form=form, model_name='ship', operation='Create')


@app.route('/index/ship/update/<int:rec_id>', methods=['GET', 'POST'])
def ship_update(rec_id: int = None):
    ship = Ship.query.get(rec_id)
    if not ship:
        return
    form = ShipForm(obj=ship)
    print(form.__dict__)
    if form.validate_on_submit():
        form.populate_obj(ship)
        print(ship, ship.code)
        session.commit()
        return redirect(url_for('ship_view'))
    return render_template('multiform.html', form=form, model_name='ship', operation='Update')


@app.route('/index/ship/delete/<int:rec_id>', methods=['GET', 'POST'])
def ship_delete(rec_id: int = None):
    ship = Ship.query.get(rec_id)
    if not ship:
        return
    session.delete(ship)
    session.commit()
    return redirect(url_for('ship_view'))


@app.route('/index/ship_type', methods=['GET', 'POST'])
@app.route('/index/ship_type/<int:rec_id>')
def ship_type_view(rec_id: int = None):
    model = ShipType
    print('ship types called with id:', rec_id or 'none')
    stype_cols = get_web_columns(model)
    cap_headers = format_headers(stype_cols)
    stype_data = get_json_data(model=model, columns=stype_cols, id=rec_id)
    print('ship type data', stype_data)
    authenticated = current_user.is_authenticated
    return render_template('registry.html', title='Ship Types', headers=stype_cols, data=stype_data,
                           cap_headers=cap_headers, authenticated=authenticated, model_name='ship_type')


@app.route('/index/ship_type/create', methods=['GET', 'POST'])
def ship_type_create():
    form = ShipTypeForm()
    print(form.__dict__)
    if form.validate_on_submit():
        ship_type = ShipType()
        form.populate_obj(ship_type)
        print(ship_type, ship_type.code)
    return render_template('multiform.html', form=form, model_name='ship_type', operation='Create')


@app.route('/index/ship_type/update/<int:rec_id>', methods=['GET', 'POST'])
def ship_type_update(rec_id: int = None):
    ship_type = ShipType.query.get(rec_id)
    if not ship_type:
        return
    form = ShipTypeForm(obj=ship_type)
    print(form.__dict__)
    if form.validate_on_submit():
        form.populate_obj(ship_type)
        print(ship_type, ship_type.code)
        session.commit()
        return redirect(url_for('ship_type_view'))
    return render_template('multiform.html', form=form, model_name='ship_type', operation='Update')


@app.route('/index/ship_type/delete/<int:rec_id>', methods=['GET', 'POST'])
def ship_type_delete(rec_id: int = None):
    ship_type = ShipType.query.get(rec_id)
    if not ship_type:
        return
    session.delete(ship_type)
    session.commit()
    return redirect(url_for('ship_type_view'))


@app.route('/index/ship_status', methods=['GET', 'POST'])
@app.route('/index/ship_status/<int:rec_id>')
def ship_status_view(rec_id: int = None):
    print('ship types called with id:', rec_id or 'none')
    stat_cols = get_web_columns(ShipStatus)
    cap_headers = format_headers(stat_cols)
    stat_data = get_json_data(model=ShipStatus, columns=stat_cols, id=rec_id)
    print('ship type data', stat_data)
    authenticated = current_user.is_authenticated
    return render_template('registry.html', title='Ship Statuses', headers=stat_cols, data=stat_data,
                           cap_headers=cap_headers, authenticated=authenticated, model_name='ship_status')


@app.route('/index/ship_status/create', methods=['GET', 'POST'])
def ship_status_create():
    form = ShipStatusForm()
    print(form.__dict__)
    if form.validate_on_submit():
        ship_status = ShipStatus()
        form.populate_obj(ship_status)
        print(ship_status, ship_status.code)
    return render_template('multiform.html', form=form, model_name='ship_status', operation='Create')


@app.route('/index/ship_status/update/<int:rec_id>', methods=['GET', 'POST'])
def ship_status_update(rec_id: int = None):
    ship_status = ShipStatus.query.get(rec_id)
    if not ship_status:
        return
    form = ShipStatusForm(obj=ship_status)
    print(form.__dict__)
    if form.validate_on_submit():
        form.populate_obj(ship_status)
        print(ship_status, ship_status.code)
        session.commit()
        return redirect(url_for('ship_status_view'))
    return render_template('multiform.html', form=form, model_name='ship_status', operation='Update')


@app.route('/index/ship_status/delete/<int:rec_id>', methods=['GET', 'POST'])
def ship_status_delete(rec_id: int = None):
    ship_status = ShipStatus.query.get(rec_id)
    if not ship_status:
        return
    session.delete(ship_status)
    session.commit()
    return redirect(url_for('ship_status_view'))


@app.route('/index/engine', methods=['GET', 'POST'])
@app.route('/index/engine/<int:rec_id>', methods=['GET', 'POST'])
def engine_view(rec_id: int = None):
    model = Engine
    engine_cols = get_web_columns(model)
    cap_headers = format_headers(engine_cols)
    engine_data = get_json_data(model=model, columns=engine_cols, id=rec_id)
    authenticated = current_user.is_authenticated
    return render_template('registry.html', title='Engines', headers=engine_cols, data=engine_data,
                           cap_headers=cap_headers, authenticated=authenticated, model_name='engine')


@app.route('/index/engine/create', methods=['GET', 'POST'])
def engine_create():
    form = EngineForm()
    print(form.__dict__)
    if form.validate_on_submit():
        engine = Engine()
        form.populate_obj(engine)
        print(engine, engine.code)
    return render_template('multiform.html', form=form, model_name='engine', operation='Create')


@app.route('/index/engine/update/<int:rec_id>', methods=['GET', 'POST'])
def engine_update(rec_id: int = None):
    engine = Engine.query.get(rec_id)
    if not engine:
        return
    form = EngineForm(obj=engine)
    print(form.__dict__)
    if form.validate_on_submit():
        form.populate_obj(engine)
        print(engine, engine.code)
        session.commit()
        return redirect(url_for('engine_view'))
    return render_template('multiform.html', form=form, model_name='engine', operation='Update')


@app.route('/index/engine/delete/<int:rec_id>', methods=['GET', 'POST'])
def engine_delete(rec_id: int = None):
    engine = Engine.query.get(rec_id)
    if not engine:
        return
    session.delete(engine)
    session.commit()
    return redirect(url_for('engine_view'))


@app.route('/index/builder', methods=['GET', 'POST'])
@app.route('/index/builder/<int:rec_id>', methods=['GET', 'POST'])
def builder_view(rec_id: int = None):
    model = Builder
    builder_cols = get_web_columns(model)
    cap_headers = format_headers(builder_cols)
    builder_data = get_json_data(model=model, columns=builder_cols, id=rec_id)
    authenticated = current_user.is_authenticated
    return render_template('registry.html', title='Builders', headers=builder_cols, data=builder_data,
                           cap_headers=cap_headers, authenticated=authenticated, model_name='builder')


@app.route('/index/builder/create', methods=['GET', 'POST'])
def builder_create():
    form = BuilderForm()
    print(form.__dict__)
    return render_template('multiform.html', form=form, model_name='builder', operation='Create')


@app.route('/index/builder/update/<int:rec_id>', methods=['GET', 'POST'])
def builder_update(rec_id: int = None):
    builder = Builder.query.get(rec_id)
    if not builder:
        return
    form = BuilderForm(obj=builder)
    print(form.__dict__)
    if form.validate_on_submit():
        form.populate_obj(builder)
        print(builder, builder.code)
        session.commit()
        return redirect(url_for('builder_view'))
    return render_template('multiform.html', form=form, model_name='builder', operation='Update')


@app.route('/index/builder/delete/<int:rec_id>', methods=['GET', 'POST'])
def builder_delete(rec_id: int = None):
    builder = Builder.query.get(rec_id)
    if not builder:
        return
    session.delete(builder)
    session.commit()
    return redirect(url_for('builder_view'))


@app.route('/gate', methods=['GET', 'POST'])
def login():
    print('gate called')
    if current_user.is_authenticated:
        return redirect(url_for('index'))
    form = LoginForm()
    print(form.__dict__)
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
    if current_user.is_authenticated:
        return render_template('user_profile.html', user=current_user)
    else:
        return redirect(url_for('login'))


print(__name__)
