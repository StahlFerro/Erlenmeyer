from pprint import pprint
from collections import OrderedDict
from typing import Dict, List, Any

from server.utils.orm import get_api_columns

from cerberus import Validator
from flask_sqlalchemy import inspect, orm


# def get_schema(model, operation) -> Dict[str, Dict[str, Any]]:
#     columns = get_api_columns(model, operation)
#     print('==== Obtained API columns ====')
#     pprint(columns)
#     schema = OrderedDict()
#     for col in columns:
#         colname = col['name']
#         schema[colname] = {'type': col['type'], 'required': col['required']}
#         if colname == 'id':
#             schema[colname].update({'min': 1})
#         if 'empty' in col.keys() and not col['empty']:
#             schema[colname].update({'empty': False})
#         if col['maxlength']:
#             schema[colname].update({'maxlength': col['maxlength']})
#     print('==== Obtained schema ====')
#     pprint(schema)
#     return schema


def get_schema(model, operation) -> Dict[str, Dict[str, Any]]:
    """ Creates a cerberus schema for view, create and update operations """
    mapper: orm.mapper = inspect(model)
    schema = OrderedDict()
    for col in mapper.columns:
        field = col.key
        ftype = col.type.__visit_name__

        if field == 'id' and operation == 'create':
            continue
        schema[field] = {'type': ftype}

        if field == 'id':
            schema[field].update({'min': 1})

        if ftype == 'string':
            schema[field].update({'maxlength': col.type.length})
            if not col.nullable:
                schema[field].update({'empty': False})

        if (operation == 'update' and field == 'id') or operation != 'update':
            schema[field].update({'required': not col.nullable})

        # rules = {
        #     'name': col.key,
        #     'type': col.type.__visit_name__,
        #     'maxlength': col.type.length if col.type.__visit_name__ == 'string' else None,
        #     'required': not col.nullable
        # }
        # if not update:
        #     rules.update({'required': not col.nullable})
        # if rules['type'] == 'string' and not col.nullable:
        #     rules['empty'] = False
        # print("RULES", rules)
    print('Obtained schema')
    pprint(schema)
    return schema


def validate_request(request, schema: dict, update=False) -> (bool, dict):
    v = Validator()
    if type(request) is not dict:
        return False, {"InvalidJSON": "A list of objects should be passed"}
    is_valid = v.validate(request, schema, update=update)
    errors = v.errors
    if errors:
        print(f'Cerberus request bork!')
        pprint(errors)
    return is_valid, errors
