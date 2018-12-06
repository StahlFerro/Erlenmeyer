from pprint import pprint
from collections import OrderedDict
from cerberus import Validator
from server.utils.orm_helpers import get_api_columns


def get_schema(model):
    columns = get_api_columns(model, include_type=True, include_limit=True)
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


def validate_request(request: dict, schema: dict) -> (bool, dict):
    v = Validator()
    is_valid = v.validate(request, schema)
    errors = v.errors
    return is_valid, errors
