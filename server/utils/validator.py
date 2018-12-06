from pprint import pprint
from collections import OrderedDict
from cerberus import Validator
from server.utils.orm_helpers import get_api_columns


def get_schema(model, method: str):
    method = str.upper(method)
    columns = get_api_columns(model, include_type=True, for_schema=True)
    print('==== Get Schema obtained columns ====')
    pprint(columns)
    schema = OrderedDict()
    if method in ['POST', 'PUT']:
        for col in columns:
            schema[col['name']] = {'type': col['type'], 'required': col['required']}
            if col['name'] == 'id':
                schema[col['name']].update({'min': 1})
            if col['maxlength']:
                schema[col['name']].update({'maxlength': col['maxlength']})
    elif method in ['DELETE']:
        id_col = [col for col in columns if col['name'] == 'id'][0]
        schema[id_col['name']] = {'type': id_col['type'], 'required': id_col['required'], 'min': 1}
    elif method in ['GET']:
        return schema
    print('==== Obtained schema ====')
    pprint(schema)
    return schema


def validate_request(request: dict, schema: dict) -> (bool, dict):
    v = Validator()
    is_valid = v.validate(request, schema)
    errors = v.errors
    if errors:
        print(f'Cerberus request bork!')
        pprint(errors)
    return is_valid, errors
