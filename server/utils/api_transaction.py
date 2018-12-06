from pprint import pprint
from server import db, session
from server.utils.validator import validate_request


def create_records(model, docs, schema) -> (dict, int):
    errors_list = []
    for doc in docs:
        is_valid, errors = validate_request(doc, schema)
        if not is_valid:
            errors_list.append(errors)
    if errors_list:
        return errors_list, 400
    else:
        new_records = []
        for doc in docs:
            record = model(**doc)
            new_records.append(record)
        print(f'created {model}:', new_records)
        for record in new_records:
            session.add(record)
        try:
            session.commit()
            return {'success': f'Added {len(new_records)} {model} records'}, 200
        except Exception as e:
            session.rollback()
            if e is Exception:
                exmsg = e.message
            else:
                exmsg = str(e.__cause__)
            errors_list.append(exmsg)
            print('>>> Transaction fail with below exception')
            pprint(e.__repr__())
            return {e.__class__.__name__: errors_list}, 400
