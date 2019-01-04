import time
from pprint import pprint

from server import db, session
from server.utils.orm import get_json_data, get_api_columns
from server.utils.validator import get_schema, validate_request


def get_records(model, id=None):
    model_name = model.__name__
    data = get_json_data(model, get_api_columns(model), id, web_api=True)
    if not any(data):
        return {"NotFoundError": f"{model_name} with id {id} does not exist"}, 404
    return data, 200


def create_records(model, docs) -> (dict, int):
    if not docs:
        return {"message": "Request body cannot be empty"}, 400
    model_name = model.__name__
    schema = get_schema(model, operation='create')
    for doc in docs:
        is_valid, errors = validate_request(doc, schema)
        if not is_valid:
            return errors, 400
        new_records = []
        for doc in docs:
            record = model(**doc)
            new_records.append(record)
        print(f'Created {model}:', new_records)
        for record in new_records:
            session.add(record)
        try:
            session.commit()
            return {"Success": f"Added {len(new_records)} {model_name} ",
                    "ids": [rec.id for rec in new_records]}, 200
        except Exception as e:
            session.rollback()
            if e is Exception:
                exmsg = e.message
            else:
                exmsg = str(e.__cause__)
            print(f"{model_name} update failed with below exception")
            pprint(e.__repr__())
            return {e.__class__.__name__: exmsg}, 400


def update_records(model, docs) -> (dict, int):
    if not docs:
        return {"message": "Request body cannot be empty"}, 400
    model_name = model.__name__
    schema = get_schema(model, operation='update')
    for doc in docs:
        print('doc', doc)
        is_valid, errors = validate_request(doc, schema)
        if not is_valid:
            return errors, 400
    doc_ids = list(set(doc["id"] for doc in docs))  # Eliminates looping through multiple ids
    all_ids = [record.id for record in model.query.all()]
    non_existing_ids = list(set(doc_ids) - set(all_ids))
    print('docids, allids, nonexids', doc_ids, all_ids, non_existing_ids)
    if non_existing_ids:
        return {"NotFoundError": f"{model_name} ids {list(non_existing_ids)} does not exist"}, 404
    try:
        for doc_id in doc_ids:
            doc = next(d for d in docs if d["id"] == doc_id)  # In case multiple docs with same id, only get one
            res = model.query.filter(model.id == doc_id).update(doc)
            print('targetdoc', doc)
        session.commit()
        return {"Success": f"Updated {len(docs)} {model_name} records: {doc_ids}"}, 200
    except Exception as e:
        session.rollback()
        if e is Exception:
            exmsg = e.message
        else:
            exmsg = str(e.__cause__)
        print(f"{model_name} update failed with below exception")
        pprint(e.__repr__())
        return {e.__class__.__name__: exmsg}, 400


def delete_record(model, id: int) -> (dict, int):
    model_name = model.__name__
    target_model = model.query.get(id)
    if not target_model:
        return {"NotFoundError": f"{model_name} with id {id} does not exist"}, 404
    try:
        session.delete(target_model)
        session.commit()
        return {"Success": f"Deleted {model_name} with id {id}"}, 200
    except Exception as e:
        session.rollback()
        if e is Exception:
            exmsg = e.message
        else:
            exmsg = str(e.__cause__)
        print(f"{model_name} update failed with below exception")
        pprint(e.__repr__())
        return {e.__class__.__name__: exmsg}, 400
