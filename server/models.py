from pydoc import locate
from pprint import pprint

from passlib.hash import argon2
from flask_login import UserMixin

from server import db, login


class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(20), index=True, unique=True)
    password_hash = db.Column(db.String(128))

    def __repr__(self):
        return f"<User {self.username}>"

    def set_password(self, password: str):
        self.password_hash = argon2.using(salt_len=40, rounds=4).hash(password)

    def check_password(self, password: str):
        return argon2.verify(password, self.password_hash)


@login.user_loader
def load_user(id):
    return User.query.get(int(id))


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
