from datetime import datetime

from werkzeug.urls import url_parse
from flask_login import current_user, login_user, logout_user
from flask import request, render_template, redirect, jsonify, flash, url_for, abort

from server import app
from server.models import Ship, ShipType, ShipStatus, Engine, Builder
from server.forms import ShipForm, ShipTypeForm, ShipStatusForm, EngineForm, BuilderForm
from server.utils.web_controller import view_records, create_records, update_records, delete_records


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
    data, headers, cap_headers = view_records(Ship, rec_id)
    authenticated = current_user.is_authenticated
    return render_template('registry.html', title='Ships', data=data, headers=headers, cap_headers=cap_headers,
                           authenticated=authenticated, model_name='ship')


@app.route('/index/ship/create', methods=['GET', 'POST'])
def ship_create():
    if not current_user.is_authenticated:
        return redirect(url_for('login'))
    form = ShipForm()
    print(form.__dict__)
    if form.validate_on_submit():
        success, msg = create_records(Ship, form)
        flash(msg)
        if success:
            return redirect(url_for('ship_view'))
    return render_template('multiform.html', form=form, model_name='ship', operation='Create')


@app.route('/index/ship/update/<int:rec_id>', methods=['GET', 'POST'])
def ship_update(rec_id: int = None):
    if not current_user.is_authenticated:
        return redirect(url_for('login'))
    ship = Ship.query.get(rec_id)
    if not ship:
        abort(404)
    form = ShipForm(obj=ship)
    print(form.__dict__)
    if form.validate_on_submit():
        status, msg = update_records(ship, form)
        flash(msg)
        return redirect(url_for('ship_view'))
    return render_template('multiform.html', form=form, model_name='ship', operation='Update')


@app.route('/index/ship/delete/<int:rec_id>', methods=['GET', 'POST'])
def ship_delete(rec_id: int = None):
    if not current_user.is_authenticated:
        return redirect(url_for('login'))
    ship = Ship.query.get(rec_id)
    if not ship:
        abort(404)
    success, msg = delete_records(ship)
    flash(msg)
    return redirect(url_for('ship_view'))


@app.route('/index/ship_type', methods=['GET', 'POST'])
@app.route('/index/ship_type/<int:rec_id>')
def ship_type_view(rec_id: int = None):
    data, headers, cap_headers = view_records(ShipType, rec_id)
    authenticated = current_user.is_authenticated
    return render_template('registry.html', title='Ship Types', data=data, headers=headers, cap_headers=cap_headers,
                           authenticated=authenticated, model_name='ship_type')


@app.route('/index/ship_type/create', methods=['GET', 'POST'])
def ship_type_create():
    if not current_user.is_authenticated:
        return redirect(url_for('login'))
    form = ShipTypeForm()
    print(form.__dict__)
    if form.validate_on_submit():
        success, msg = create_records(ShipType, form)
        flash(msg)
        if success:
            return redirect(url_for('ship_type_view'))
    return render_template('multiform.html', form=form, model_name='ship_type', operation='Create')


@app.route('/index/ship_type/update/<int:rec_id>', methods=['GET', 'POST'])
def ship_type_update(rec_id: int = None):
    if not current_user.is_authenticated:
        return redirect(url_for('login'))
    ship_type = ShipType.query.get(rec_id)
    if not ship_type:
        abort(404)
    form = ShipTypeForm(obj=ship_type)
    print(form.__dict__)
    if form.validate_on_submit():
        status, msg = update_records(ship_type, form)
        flash(msg)
        return redirect(url_for('ship_type_view'))
    return render_template('multiform.html', form=form, model_name='ship_type', operation='Update')


@app.route('/index/ship_type/delete/<int:rec_id>', methods=['GET', 'POST'])
def ship_type_delete(rec_id: int = None):
    if not current_user.is_authenticated:
        return redirect(url_for('login'))
    ship_type = ShipType.query.get(rec_id)
    if not ship_type:
        abort(404)
    success, msg = delete_records(ship_type)
    flash(msg)
    return redirect(url_for('ship_type_view'))


@app.route('/index/ship_status', methods=['GET', 'POST'])
@app.route('/index/ship_status/<int:rec_id>')
def ship_status_view(rec_id: int = None):
    data, headers, cap_headers = view_records(ShipStatus, rec_id)
    authenticated = current_user.is_authenticated
    return render_template('registry.html', title='Ship Statuses', data=data, headers=headers, cap_headers=cap_headers,
                           authenticated=authenticated, model_name='ship_status')


@app.route('/index/ship_status/create', methods=['GET', 'POST'])
def ship_status_create():
    if not current_user.is_authenticated:
        return redirect(url_for('login'))
    form = ShipStatusForm()
    print(form.__dict__)
    if form.validate_on_submit():
        success, msg = create_records(ShipStatus, form)
        flash(msg)
        if success:
            return redirect(url_for('ship_status_view'))
    return render_template('multiform.html', form=form, model_name='ship_status', operation='Create')


@app.route('/index/ship_status/update/<int:rec_id>', methods=['GET', 'POST'])
def ship_status_update(rec_id: int = None):
    if not current_user.is_authenticated:
        return redirect(url_for('login'))
    ship_status = ShipStatus.query.get(rec_id)
    if not ship_status:
        abort(404)
    form = ShipStatusForm(obj=ship_status)
    print(form.__dict__)
    if form.validate_on_submit():
        status, msg = update_records(ship_status, form)
        flash(msg)
        return redirect(url_for('ship_status_view'))
    return render_template('multiform.html', form=form, model_name='ship_status', operation='Update')


@app.route('/index/ship_status/delete/<int:rec_id>', methods=['GET', 'POST'])
def ship_status_delete(rec_id: int = None):
    if not current_user.is_authenticated:
        return redirect(url_for('login'))
    ship_status = ShipStatus.query.get(rec_id)
    if not ship_status:
        abort(404)
    success, msg = delete_records(ship_status)
    flash(msg)
    return redirect(url_for('ship_status_view'))


@app.route('/index/engine', methods=['GET', 'POST'])
@app.route('/index/engine/<int:rec_id>', methods=['GET', 'POST'])
def engine_view(rec_id: int = None):
    data, headers, cap_headers = view_records(Engine, rec_id)
    authenticated = current_user.is_authenticated
    return render_template('registry.html', title='Engines', data=data, headers=headers, cap_headers=cap_headers,
                           authenticated=authenticated, model_name='engine')


@app.route('/index/engine/create', methods=['GET', 'POST'])
def engine_create():
    if not current_user.is_authenticated:
        return redirect(url_for('login'))
    form = EngineForm()
    if form.validate_on_submit():
        success, msg = create_records(Engine, form)
        flash(msg)
        if success:
            return redirect(url_for('engine_view'))
    return render_template('multiform.html', form=form, model_name='engine', operation='Create')


@app.route('/index/engine/update/<int:rec_id>', methods=['GET', 'POST'])
def engine_update(rec_id: int = None):
    if not current_user.is_authenticated:
        return redirect(url_for('login'))
    engine = Engine.query.get(rec_id)
    if not engine:
        abort(404)
    form = EngineForm(obj=engine)
    if form.validate_on_submit():
        status, msg = update_records(engine, form)
        flash(msg)
        return redirect(url_for('engine_view'))
    return render_template('multiform.html', form=form, model_name='engine', operation='Update')


@app.route('/index/engine/delete/<int:rec_id>', methods=['GET', 'POST'])
def engine_delete(rec_id: int = None):
    if not current_user.is_authenticated:
        return redirect(url_for('login'))
    engine = Engine.query.get(rec_id)
    if not engine:
        abort(404)
    success, msg = delete_records(engine)
    flash(msg)
    return redirect(url_for('engine_view'))


@app.route('/index/builder', methods=['GET', 'POST'])
@app.route('/index/builder/<int:rec_id>', methods=['GET', 'POST'])
def builder_view(rec_id: int = None):
    data, headers, cap_headers = view_records(Builder, rec_id)
    authenticated = current_user.is_authenticated
    return render_template('registry.html', title='Builders', data=data, headers=headers, cap_headers=cap_headers,
                           authenticated=authenticated, model_name='builder')


@app.route('/index/builder/create', methods=['GET', 'POST'])
def builder_create():
    if not current_user.is_authenticated:
        return redirect(url_for('login'))
    form = BuilderForm()
    if form.validate_on_submit():
        success, msg = create_records(Builder, form)
        flash(msg)
        if success:
            return redirect(url_for('builder_view'))
    return render_template('multiform.html', form=form, model_name='builder', operation='Create')


@app.route('/index/builder/update/<int:rec_id>', methods=['GET', 'POST'])
def builder_update(rec_id: int = None):
    if not current_user.is_authenticated:
        return redirect(url_for('login'))
    builder = Builder.query.get(rec_id)
    if not builder:
        abort(404)
    form = BuilderForm(obj=builder)
    print(form.__dict__)
    if form.validate_on_submit():
        status, msg = update_records(builder, form)
        flash(msg)
        return redirect(url_for('builder_view'))
    return render_template('multiform.html', form=form, model_name='builder', operation='Update')


@app.route('/index/builder/delete/<int:rec_id>', methods=['GET', 'POST'])
def builder_delete(rec_id: int = None):
    if not current_user.is_authenticated:
        return redirect(url_for('login'))
    builder = Builder.query.get(rec_id)
    if not builder:
        abort(404)
    success, msg = delete_records(builder)
    flash(msg)
    return redirect(url_for('builder_view'))


print(__name__)
