import json
from pprint import pprint
from datetime import date, datetime
from typing import List, Dict, Any

from flask_sqlalchemy import inspect, orm, DefaultMeta


def get_web_columns(model, headers_override=None) -> List[str]:
    mapper: orm.mapper = inspect(model)
    columns = [col.key for col in mapper.attrs if ('_id' not in col.key and '_ids' not in col.key)]
    # columns.remove('id')  # Id is needed for url endpoints
    print('columns', columns)
    if headers_override:
        if 'id' not in headers_override:
            headers_override.append('id')
        columns = headers_override
    return columns


def get_api_columns(model, include_type=False):
    mapper = inspect(model)
    exceptions = []
    if include_type:
        columns = [(col.key, col.type.__visit_name__) for col in mapper.columns if col.key not in exceptions]
    else:
        columns = [col.key for col in mapper.columns if col.key not in exceptions]
    print('Obtained api columns')
    pprint(columns)
    return columns


# def positive_int(value):
#     intval = int(value)
#     if intval < 1:
#         raise TypeError(f"Id {value} is not a valid id! (should be greater than 0)")
#     return intval


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


def get_json_data(model, columns, id=None, web_api=False) -> List[Dict[str, Any]]:
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
    # pprint('all json')
    # pprint(out_json)
    out_json.sort(key=lambda i: i['id'])
    return out_json


def format_headers(headers):
    """
    Return a list of column names formatted as headers
    :param headers:
    :return list:
    """
    new_headers = []
    for h in headers:
        h: str = h
        if '_' in h:
            h = h.replace('_', ' ')
        # if 'id' in h:
        #     h = h.replace('id', '')
        h = h.strip()
        h = h.capitalize()
        if h == 'Power output':
            h = 'Power output (kW)'
        elif h == 'Ship type':
            h = 'Type'
        elif h == 'Ship status':
            h = 'Status'
        elif h == 'Speed':
            h = 'Speed (kn)'
        new_headers.append(h)
    return new_headers
