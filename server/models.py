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


class Ship(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(40), index=True)
    code = db.Column(db.String(5), index=True)
    speed = db.Column(db.Float)
    capacity = db.Column(db.Integer)
    launch_date = db.Column(db.Date)
    engine_id = db.Column(db.Integer, db.ForeignKey('engine.id'))

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


def get_columns(model=None):
    mapper: orm.mapper = inspect(model)
    columns = [col.key for col in mapper.attrs if ('_id' not in col.key and '_ids' not in col.key)]
    columns.remove('id')
    print('columns', columns)
    return columns

def get_cols_dual(model=None):
    mapper: orm.mapper = inspect(model)
    # print('mapper columns', [c.key for c in mapper.columns])
    # print('mapper attrs', [x.key for x in mapper.attrs])   # _ids removed (one2many fields)
    # column_names = [col.key for col in mapper.columns]
    # column_names = [col.key for col in mapper.attrs if ('_id' not in col.key and '_ids' not in col.key)]
    # column_names = [col.key for col in mapper.attrs if '_ids' not in col.key]
    columns = [col for col in mapper.attrs if (col.key != 'id' and '_ids' not in col.key)]
    print('allcol', [col for col in mapper.attrs])
    normal_cols = [nc.key for nc in columns if '_id' not in nc.key and type(nc) is ColumnProperty]
    relation_cols = [rc.key for rc in columns if type(rc) is RelationshipProperty]
    print('n and c cols', normal_cols, relation_cols)
    return normal_cols, relation_cols
    # column_names.remove('id')  # Get rid of id column
    # print('final column names', column_names)
    # return column_names


def get_json_data(model=None, columns=None, id=None):
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
            print(type(type(val)))
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
                elif type(type(val)) is DefaultMeta:
                    data[col] = [val.name, f"/index/{col}s/{val.id}"]
                else:
                    data[col] = ''
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
