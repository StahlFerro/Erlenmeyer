from server import db, login
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin
from flask_sqlalchemy import inspect
from flask_sqlalchemy import DeclarativeMeta
from datetime import date, datetime
from pprint import pprint
import json


class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(20), index=True)
    password_hash = db.Column(db.String(128))

    def __repr__(self):
        return f"<User {self.username}>"

    def hash_password(self, password: str):
        return generate_password_hash(password)

    def set_password(self, password: str):
        self.password_hash = generate_password_hash(password)

    def check_password(self, password: str):
        return check_password_hash(self.password_hash, password)


@login.user_loader
def load_user(id):
    return User.query.get(int(id))


class Ship(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(40), index=True)
    code = db.Column(db.String(5), index=True)
    speed = db.Column(db.Float)
    launch_date = db.Column(db.Date)

    def __repr__(self):
        return f"<Ship [{self.code}] {self.name}>"


def get_cols(model=None):
    mapper = inspect(model)
    column_names = [col.key for col in mapper.attrs]
    column_names.remove('id')
    return column_names


def get_json_data(model=None, columns=None):
    if not columns:
        columns = get_cols(model)
    ships = model.query.all()
    print('ships', ships)
    out_json = []
    index = 1
    for ship in ships:
        cols = [f for f in dir(ship) if f in columns]
        record = {}
        for col in cols:
            val = ship.__getattribute__(col)
            print('raw val', val)
            try:
                json.dumps(val)
                record[col] = val
            except TypeError:
                if type(val) is date:
                    val: date = val.strftime('%Y-%m-%d')
                    record[col] = val
                elif type(val) is datetime:
                    val: datetime = val.strftime('%Y-%m-%d %H:%M:%S')
                    record[col] = val
                else:
                    record[col] = ''
        record['index'] = index
        index += 1
        out_json.append(record)
    pprint(out_json)
    return out_json


def capitalize_headers(headers: list = None):
    new_headers = []
    if not headers:
        return new_headers
    for h in headers:
        if '_' in h:
            h = h.replace('_', ' ')
        h = h.capitalize()
        new_headers.append(h)
    return new_headers

# class AlchemyEncoder(json.JSONEncoder):
#     def default(self, obj):
#         print('obj name', obj)
#         if isinstance(obj.__class__, DeclarativeMeta):
#             # an SQLAlchemy class
#             fields = {}
#             # print('obj dir', dir(obj))
#             for field in [x for x in dir(obj) if not x.startswith('_') and x != 'metadata']:
#                 data = obj.__getattribute__(field)
#                 try:
#                     # print('data before', data)
#                     json.dumps(data)  # this will fail on non-encodable values, like other classes
#                     # print('data after', data)
#                     fields[field] = data
#                 except TypeError:
#                     fields[field] = None
#             # a json-encodable dict
#             # pprint('dinal fields')
#             # pprint(fields)
#             return fields
#
#         return json.JSONEncoder.default(self, obj)
