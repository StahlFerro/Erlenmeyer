from pydoc import locate
from server import db, login
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin
from flask_sqlalchemy import inspect, orm, DeclarativeMeta, DefaultMeta
from sqlalchemy.orm.properties import ColumnProperty, RelationshipProperty
from datetime import date, datetime
from pprint import pprint
import json


class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(20), index=True)
    password_hash = db.Column(db.String(128))

    def __repr__(self):
        return f"<User {self.username}>"

    def set_password(self, password: str):
        self.password_hash = generate_password_hash(password)

    def check_password(self, password: str):
        return check_password_hash(self.password_hash, password)


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
    ship_ids = db.relationship('Ship', backref='ship_status', lazy='dynamic')

    def __repr__(self):
        return f"<ShipStatus [{self.name}]>"


class Ship(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(40), index=True)
    code = db.Column(db.String(5), index=True)
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
    code = db.Column(db.String(5), index=True)
    power_output = db.Column(db.Float)
    type = db.Column(db.String(60))
    ship_ids = db.relationship('Ship', backref='engine', lazy='dynamic')

    def __repr__(self):
        return f"<Engine [{self.code}] {self.name}>"


class Builder(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(40), index=True)
    code = db.Column(db.String(5), index=True)
    date_founded = db.Column(db.Date)
    founder = db.Column(db.String(40))
    headquarters = db.Column(db.String(40))
    ship_ids = db.relationship('Ship', backref='builder', lazy='dynamic')

    def __repr__(self):
        return f"<Builder [{self.code}] {self.name}>"


def get_web_columns(model):
    mapper: orm.mapper = inspect(model)
    columns = [col.key for col in mapper.attrs if ('_id' not in col.key and '_ids' not in col.key)]
    columns.remove('id')
    print('columns', columns)
    return columns


def get_api_columns(model, include_type=False):
    mapper = inspect(model)
    if include_type:
        columns = [(col.key, get_type(type(col.type).__visit_name__)) for col in mapper.columns]
    else:
        columns = [col.key for col in mapper.columns]
    print('columns', columns)
    return columns


def get_type(text: str):
    if text == 'string':
        return str
    elif text == 'integer':
        return int
    elif text == 'date':
        return date
    elif text == 'datetime':
        return datetime
    else:
        return locate(text)


def get_json_data(model, columns, id=None, web_api=False):
    if id:
        records = [model.query.get(id)]
    else:
        records = model.query.all()
    out_json = []
    index = 1
    for record in records:
        cols = [f for f in dir(record) if f in columns]
        data = {}
        for col in cols:
            # print(cols)
            val = record.__getattribute__(col)
            # print(type(type(val)))
            try:
                json.dumps(val)
                data[col] = val
            except TypeError:
                if type(val) is date:  # is a date obj
                    val: date = val.strftime('%Y-%m-%d')
                    data[col] = val
                elif type(val) is datetime:  # is a datetime obj
                    val: datetime = val.strftime('%Y-%m-%d %H:%M:%S')
                    data[col] = val
                elif type(type(val)) is DefaultMeta:  # is an sqlaclhemy obj
                    # if col[-1] in ('s', 'x'):
                    #     route_url = f"{col}es"
                    # else:
                    #     route_url = f"{col}s"
                    data[col] = [val.name, f"/index/{col}/{val.id}"]
                else:
                    data[col] = ''
        if not web_api:
            data['index'] = index
        index += 1
        out_json.append(data)
    pprint('all json')
    pprint(out_json)
    return out_json


def format_headers(headers: list = None):
    """
    Return a list of column names formatted as headers
    :param headers:
    :return list:
    """
    new_headers = []
    if not headers:
        return new_headers
    print('new headers', headers)
    for h in headers:
        h: str = h
        if '_' in h:
            h = h.replace('_', ' ')
        if 'id' in h:
            h = h.replace('id', '')
        h = h.strip()
        h = h.capitalize()
        if h == 'Power output':
            h = 'Power output (kW)'
        elif h == 'Ship type':
            h = 'Type'
        elif h == 'Ship status':
            h = 'Status'
        new_headers.append(h)
    return new_headers


print(__name__)
