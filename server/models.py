from pydoc import locate
from pprint import pprint
from datetime import datetime, timedelta
import secrets

from passlib.hash import argon2
from flask_login import UserMixin
from flask_jwt_extended import create_access_token, create_refresh_token, get_raw_jwt, get_csrf_token
from flask import request

from server import db, login, jwt


class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(20), index=True, unique=True, nullable=False)
    password_hash = db.Column(db.String(128))
    client_secret = db.Column(db.String(128))
    token_hash = db.Column(db.String(128))
    is_admin = db.Column(db.Boolean, default=False)
    date_created = db.Column(db.DateTime)
    last_login = db.Column(db.DateTime)

    def __init__(self):
        self.client_secret = secrets.token_urlsafe(64)  # Generate a random string for the client secret

    def __repr__(self):
        return f"<User {self.username}>"

    def set_password(self, password: str):
        self.password_hash = argon2.using(salt_len=40, rounds=4).hash(password)

    def check_password(self, password: str) -> bool:
        return argon2.verify(password, self.password_hash)

    def update_login_date(self):
        self.last_login = datetime

    def generate_access_token(self) -> str:
        token = create_access_token(self.client_secret, expires_delta=timedelta(days=30))
        self.token_hash = argon2.using(salt_len=40, rounds=4).hash(token)
        print('token generated', token)
        print('token hashed', self.token_hash)
        db.session.commit()
        return token

    def generate_refresh_token(self) -> str:
        """ UNUSED """
        return create_refresh_token(self.client_secret, expires_delta=timedelta(days=120))

    def check_token_hash(self, token: str) -> bool:
        if self.token_hash:
            return argon2.verify(token, self.token_hash)
        else:
            return False

    def generate_dual_tokens(self) -> (str, str):
        return self.generate_access_token(), self.generate_refresh_token()

    @classmethod
    def from_secret(cls, secret: str):
        return cls.query.filter_by(client_secret=secret).first()

    def reset_client_secret(self):
        new_secret = secrets.token_urlsafe(64)
        self.client_secret = new_secret
        db.session.commit()


@login.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))


@jwt.token_in_blacklist_loader
def check_if_token_blacklisted(decrypted_token):
    # print('-------{}{}{} Blacklist loader called {}{}{}-------')
    # print(decrypted_token)
    # print(get_raw_jwt())
    user = User.from_secret(decrypted_token['identity'])
    print('USER', user)
    if not user:
        return True
    else:
        token = request.headers.get('Authorization').replace('Bearer ', '')
        if not token:
            return True
        hash_success = user.check_token_hash(token)
        print('hash success: ', hash_success)
        if hash_success:
            return False  # Hash matched, token is not blacklisted
        else:
            return True  # Hash does not match, token is blacklisted


class ShipType(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(40), index=True, nullable=False)
    ship_ids = db.relationship('Ship', backref='ship_type', lazy='dynamic')

    def __repr__(self):
        return f"{self.name}"


class ShipStatus(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(40), index=True, nullable=False)
    description = db.Column(db.String(150))
    ship_ids = db.relationship('Ship', backref='ship_status', lazy='dynamic')

    def __repr__(self):
        return f"{self.name}"


class Ship(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(40), index=True)
    code = db.Column(db.String(5), index=True, unique=True, nullable=False)
    speed = db.Column(db.Float)
    capacity = db.Column(db.Integer)
    launch_date = db.Column(db.Date)
    ship_type_id = db.Column(db.Integer, db.ForeignKey('ship_type.id'))
    engine_id = db.Column(db.Integer, db.ForeignKey('engine.id'))
    builder_id = db.Column(db.Integer, db.ForeignKey('builder.id'))
    ship_status_id = db.Column(db.Integer, db.ForeignKey('ship_status.id'))

    def __repr__(self):
        return f"[{self.code}] {self.name}"

    @classmethod
    def unsigned_attrs(cls):
        """ List of column names that are unsigned integers. Will be used for the API side validation as a workaround
            for PostgreSQL's lack of support for UInts """
        return ['capacity']


class Engine(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(40), index=True)
    code = db.Column(db.String(5), index=True, unique=True, nullable=False)
    power_output = db.Column(db.Float)
    type = db.Column(db.String(60))
    ship_ids = db.relationship('Ship', backref='engine', lazy='dynamic')

    def __repr__(self):
        return f"[{self.code}] {self.name}"


class Builder(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(40), index=True)
    code = db.Column(db.String(5), index=True, unique=True, nullable=False)
    date_founded = db.Column(db.Date)
    founder = db.Column(db.String(40))
    headquarters = db.Column(db.String(40))
    ship_ids = db.relationship('Ship', backref='builder', lazy='dynamic')

    def __repr__(self):
        return f"[{self.code}] {self.name}"


print(__name__)
