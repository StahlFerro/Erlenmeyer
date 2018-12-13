from pydoc import locate
from pprint import pprint
from datetime import datetime, timedelta
import secrets

from passlib.hash import argon2
from flask_login import UserMixin
from flask_jwt_extended import create_access_token, create_refresh_token


from server import db, login, jwt


class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(20), index=True, unique=True, nullable=False)
    password_hash = db.Column(db.String(128))
    client_secret = db.Column(db.String(128))

    def __init__(self):
        self.client_secret = secrets.token_urlsafe(64)

    def __repr__(self):
        return f"<User {self.username}>"

    def set_password(self, password: str):
        self.password_hash = argon2.using(salt_len=40, rounds=4).hash(password)

    def check_password(self, password: str) -> bool:
        return argon2.verify(password, self.password_hash)

    def generate_access_token(self) -> str:
        return create_access_token(self.client_secret, expires_delta=timedelta(days=1))

    def generate_refresh_token(self) -> str:
        return create_refresh_token(self.client_secret, expires_delta=timedelta(days=1))

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
def load_user(id):
    return User.query.get(int(id))


class RevokedToken(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    jti = db.Column(db.String(128), nullable=False)

    def add(self):
        db.session.add(self)
        db.session.commit()

    @classmethod
    def is_blacklisted(cls, jti: str) -> bool:
        record = cls.query.filter_by(jti=jti).first()
        return bool(record)


@jwt.token_in_blacklist_loader
def check_if_token_blacklisted(decrypted_token):
    print('-------{}{}{} DECRYPTED TOKEN {}{}{}-------')
    token = decrypted_token['jti']
    pprint(token)
    return RevokedToken.is_blacklisted(token)


class ShipType(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(40), index=True)
    ship_ids = db.relationship('Ship', backref='ship_type', lazy='dynamic')

    def __repr__(self):
        return f"<ShipType [{self.name}]>"


class ShipStatus(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(40), index=True)
    description = db.Column(db.String(150))
    ship_ids = db.relationship('Ship', backref='ship_status', lazy='dynamic')

    def __repr__(self):
        return f"<ShipStatus [{self.name}]>"


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
        return f"<Ship [{self.code}] {self.name}>"


class Engine(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(40), index=True)
    code = db.Column(db.String(5), index=True, unique=True, nullable=False)
    power_output = db.Column(db.Float)
    type = db.Column(db.String(60))
    ship_ids = db.relationship('Ship', backref='engine', lazy='dynamic')

    def __repr__(self):
        return f"<Engine [{self.code}] {self.name}>"


class Builder(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(40), index=True)
    code = db.Column(db.String(5), index=True, unique=True, nullable=False)
    date_founded = db.Column(db.Date)
    founder = db.Column(db.String(40))
    headquarters = db.Column(db.String(40))
    ship_ids = db.relationship('Ship', backref='builder', lazy='dynamic')

    def __repr__(self):
        return f"<Builder [{self.code}] {self.name}>"


print(__name__)
