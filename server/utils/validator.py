from pprint import pprint
from collections import OrderedDict
from typing import Dict, List

from cerberus import Validator

from server.utils.orm_helpers import get_api_columns


def get_schema(model):
    columns = get_api_columns(model, include_type=True, for_schema=True)
    print('==== Get Schema obtained columns ====')
    pprint(columns)
    schema = OrderedDict()
    for col in columns:
        schema[col['name']] = {'type': col['type'], 'required': col['required']}
        if col['name'] == 'id':
            schema[col['name']].update({'min': 1})
        if col['maxlength']:
            schema[col['name']].update({'maxlength': col['maxlength']})
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
