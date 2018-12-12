import json
from pprint import pprint
from datetime import date, datetime

from flask_sqlalchemy import inspect, orm, DefaultMeta


def get_web_columns(model):
    mapper: orm.mapper = inspect(model)
    columns = [col.key for col in mapper.attrs if ('_id' not in col.key and '_ids' not in col.key)]
    columns.remove('id')
    print('columns', columns)
    return columns


def get_api_columns(model, include_type=False, for_schema=False, exclude_id=False):
    mapper = inspect(model)
    exceptions = []
    if exclude_id:
        exceptions.append('id')
    if include_type:
        if for_schema:
            columns = []
            for col in mapper.columns:
                if col.key in exceptions:
                    continue
                rules = {
                    'name': col.key,
                    'type': col.type.__visit_name__,
                    'maxlength': col.type.length if col.type.__visit_name__ == 'string' else None,
                    'required': not col.nullable
                }
                if rules['type'] == 'string' and not col.nullable:
                    rules['empty'] = False
                # print("RULES", rules)
                columns.append(rules)
        else:
            columns = [(col.key, col.type.__visit_name__) for col in mapper.columns if col.key not in exceptions]
    else:
        columns = [col.key for col in mapper.columns if col.key not in exceptions]
    print('Obtained api columns')
    pprint(columns)
    return columns


def positive_int(value):
    intval = int(value)
    if intval < 1:
        raise TypeError(f"Id {value} is not a valid id! (should be greater than 0)")
    return intval


# def get_type(text: str):
#     if text == 'string':
#         return str
#     elif text == 'integer':
#         return positive_int
#     elif text == 'date':
#         return date
#     elif text == 'datetime':
#         return datetime
#     else:
#         return locate(text)


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
