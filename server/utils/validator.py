from pprint import pprint
from collections import OrderedDict
from typing import Dict, List, Any

from cerberus import Validator

from server.utils.orm import get_api_columns


def get_schema(model, exclude_id=False) -> Dict[str, Dict[str, Any]]:
    columns = get_api_columns(model, include_type=True, for_schema=True, exclude_id=exclude_id)
    print('==== Obtained API columns ====')
    pprint(columns)
    schema = OrderedDict()
    for col in columns:
        colname = col['name']
        schema[colname] = {'type': col['type'], 'required': col['required']}
        if colname == 'id':
            schema[colname].update({'min': 1})
        if 'empty' in col.keys() and not col['empty']:
            schema[colname].update({'empty': False})
        if col['maxlength']:
            schema[colname].update({'maxlength': col['maxlength']})
    print('==== Obtained schema ====')
    pprint(schema)
    return schema


def validate_request(request, schema: dict) -> (bool, dict):
    v = Validator()
    if type(request) is not dict:
        return False, {"InvalidJSON": "A list of objects should be passed"}
    is_valid = v.validate(request, schema)
    errors = v.errors
    if errors:
        print(f'Cerberus request bork!')
        pprint(errors)
    return is_valid, errors
