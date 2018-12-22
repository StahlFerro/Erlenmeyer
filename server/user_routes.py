from datetime import datetime

from werkzeug.urls import url_parse
from flask_login import current_user, login_user, logout_user
from flask import request, render_template, redirect, flash, url_for, abort

from server import app, db, session
from server.forms import LoginForm,  UserForm, UpdatePasswordForm
from server.models import User
from server.utils.url import is_safe_url
from server.utils.web_controller import view_records, create_records, delete_records


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
            user.last_login = datetime.utcnow()
            session.commit()
            print('user last login!', user.last_login)
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


@app.route('/user_profile/user_repassword', methods=['GET', 'POST'])
def user_repassword():
    if current_user.is_authenticated:
        form = UpdatePasswordForm()
        if form.validate_on_submit():
            if current_user.check_password(form.old_password.data):
                current_user.set_password(form.new_password.data)
                session.commit()
                return redirect(url_for('user_profile'))
            else:
                flash('Invalid Old Password')
        return render_template('user_repassword.html', user=current_user, form=form, username=current_user.username)
    else:
        return redirect(url_for('login'))


@app.route('/user_profile/new_token')
def new_token_page():
    if current_user.is_authenticated:
        user = User.query.get(current_user.id)
        token = user.generate_access_token()
        return render_template('new_token.html', token=token)
    else:
        return redirect(url_for('login'))


@app.route('/users_list')
def users_view():
    authenticated = current_user.is_authenticated
    if authenticated:
        user = User.query.get(current_user.id)
        if user.is_admin:
            data, headers, cap_headers = view_records(User, headers_override=
                ['username', 'date_created', 'last_login', 'is_admin'])
            return render_template('registry.html', title='Users', data=data, headers=headers, user=current_user,
                                   cap_headers=cap_headers, authenticated=authenticated, model_name='users')
    return abort(403)


@app.route('/users_list/create', methods=['GET', 'POST'])
def users_create():
    print('bollocks')
    if current_user.is_authenticated and current_user.is_admin:
        form = UserForm()
        print('bollocks form')
        if form.validate_on_submit():
            print('success')
            success, msg = create_records(User, form)
            flash(msg)
            if success:
                return redirect(url_for('users_view'))
        return render_template('multiform.html', form=form, model_name='users', operation='Create')
    else:
        print('fail')
        return abort(403)


@app.route('/users_list/delete/<int:rec_id>', methods=['GET', 'POST'])
def users_delete(rec_id: int = None):
    if current_user.is_authenticated and current_user.is_admin:
        user = User.query.get(rec_id)
        if not user:
            return
        success, msg = delete_records(user)
        flash(msg)
        return redirect(url_for('users_view'))
    else:
        print('fail')
        return abort(403)


print(__name__)
