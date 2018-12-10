from pprint import pprint
from collections import OrderedDict

from flask_restful import Resource, reqparse, request

from server import app, api, db, session
from server.models import Ship, ShipType, ShipStatus, Engine, Builder
from server.utils.orm_helpers import get_api_columns, get_json_data
from server.utils.api_transaction import get_records, create_records, update_records, delete_record


class ShipListAPI(Resource):
    def __init__(self):
        self.model = Ship

    def get(self):
        return get_records(self.model)

    def post(self):
        print('======= POST multi test ======')
        docs = request.json
        print('Json is valid')
        pprint(docs)
        return create_records(self.model, docs)

    def put(self):
        print('======= PUT multi test ======')
        docs = request.json
        print('Json is valid')
        pprint(docs)
        return update_records(self.model, docs)


class ShipAPI(Resource):
    def __init__(self):
        self.model = Ship

    def get(self, id):
        return get_records(self.model, id)

    def delete(self, id):
        return delete_record(self.model, id)


class ShipTypeListAPI(Resource):
    def __init__(self):
        self.model = ShipType

    def get(self):
        return get_records(self.model)

    def post(self):
        print('======= POST multi test ======')
        docs = request.json
        print('Json is valid')
        pprint(docs)
        return create_records(self.model, docs)

    def put(self):
        print('======= PUT multi test ======')
        docs = request.json
        print('Json is valid')
        pprint(docs)
        return update_records(self.model, docs)


class ShipTypeAPI(Resource):
    def __init__(self):
        self.model = ShipType

    def get(self, id):
        return get_records(self.model, id)

    def delete(self, id):
        return delete_record(self.model, id)


class ShipStatusListAPI(Resource):
    def __init__(self):
        self.model = ShipStatus

    def get(self):
        return get_records(self.model)

    def post(self):
        print('======= POST multi test ======')
        docs = request.json
        print('Json is valid')
        pprint(docs)
        return create_records(self.model, docs)

    def put(self):
        print('======= PUT multi test ======')
        docs = request.json
        print('Json is valid')
        pprint(docs)
        return update_records(self.model, docs)


class ShipStatusAPI(Resource):
    def __init__(self):
        self.model = ShipStatus

    def get(self, id):
        return get_records(self.model, id)

    def delete(self, id):
        return delete_record(self.model, id)


class EngineListAPI(Resource):
    def __init__(self):
        self.model = Engine

    def get(self):
        return get_records(self.model)

    def post(self):
        print('======= POST multi test ======')
        docs = request.json
        print('Json is valid')
        pprint(docs)
        return create_records(self.model, docs)

    def put(self):
        print('======= PUT multi test ======')
        docs = request.json
        print('Json is valid')
        pprint(docs)
        return update_records(self.model, docs)


class EngineAPI(Resource):
    def __init__(self):
        self.model = Engine

    def get(self, id):
        return get_records(self.model, id)

    def delete(self, id):
        return delete_record(self.model, id)


class BuilderListAPI(Resource):
    def __init__(self):
        self.model = Engine

    def get(self):
        return get_records(self.model)

    def post(self):
        print('======= POST multi test ======')
        docs = request.json
        print('Json is valid')
        pprint(docs)
        return create_records(self.model, docs)

    def put(self):
        print('======= PUT multi test ======')
        docs = request.json
        print('Json is valid')
        pprint(docs)
        return update_records(self.model, docs)


class BuilderAPI(Resource):
    def __init__(self):
        self.model = Builder

    def get(self, id):
        return get_records(self.model, id)

    def delete(self, id):
        return delete_record(self.model, id)


api.add_resource(ShipListAPI, '/api/ships', endpoint='ships_api')
api.add_resource(ShipAPI, '/api/ships/<int:id>', endpoint='ship_api')
api.add_resource(EngineListAPI, '/api/engines', endpoint='engines_api')
api.add_resource(EngineAPI, '/api/engines/<int:id>', endpoint='engine_api')
api.add_resource(BuilderListAPI, '/api/builders', endpoint='builders_api')
api.add_resource(BuilderAPI, '/api/builders/<int:id>', endpoint='builder_api')
api.add_resource(ShipTypeListAPI, '/api/ship_types', endpoint='ship_types_api')
api.add_resource(ShipTypeAPI, '/api/ship_types/<int:id>', endpoint='ship_type_api')
api.add_resource(ShipStatusListAPI, '/api/ship_statuses', endpoint='ship_statuses_api')
api.add_resource(ShipStatusAPI, '/api/ship_statuses/<int:id>', endpoint='ship_status_api')
print(__name__)
