from datetime import datetime
from pprint import pprint

from server import session
from server.utils.orm import get_web_columns, format_headers, get_json_data
from server.models import User


css = {"yes": "is-success", "no": "is-danger"}


def view_records(model_class, rec_id: int = None, headers_override=None):
    print('models called with id:', rec_id or 'none')
    headers = get_web_columns(model_class, headers_override=headers_override)
    data = get_json_data(model=model_class, columns=headers, id=rec_id)
    cap_headers = format_headers(headers)
    return data, headers, cap_headers


def create_records(model_class, form):
    new_record = model_class()
    form.populate_obj(new_record)
    if model_class is User:
        new_record: User = new_record
        new_record.set_password(new_record.username)
        new_record.date_created = datetime.utcnow()
    try:
        session.add(new_record)
        session.commit()
        msg = (css["yes"], f"{new_record} create succeeded")
        print(msg)
        return True, msg
    except Exception as e:
        session.rollback()
        if e is Exception:
            exmsg = e.message
        else:
            exmsg = str(e.__cause__)
        print(f"{model_class} create failed with below exception")
        pprint(e.__repr__())
        return False, (css["no"], exmsg)


def update_records(model, form):
    form.populate_obj(model)
    try:
        session.commit()
        msg = (css["yes"], f"{model} update succeeded")
        print(msg)
        return True, msg
    except Exception as e:
        session.rollback()
        if e is Exception:
            exmsg = e.message
        else:
            exmsg = str(e.__cause__)
        print(f"{model} update failed with below exception")
        pprint(e.__repr__())
        return False, (css["no"], exmsg)


def delete_records(model):
    try:
        msg = (css["yes"], f"{model} delete succeeded")
        session.delete(model)
        session.commit()
        print(msg)
        return True, msg
    except Exception as e:
        session.rollback()
        if e is Exception:
            exmsg = e.message
        else:
            exmsg = str(e.__cause__)
        print(f"{model} delete failed with below exception")
        pprint(e.__repr__())
        return False, (css["no"], exmsg)
