from pprint import pprint
from server import app, api, db
from server.models import Ship, ShipType, ShipStatus, Engine, Builder, get_json_data, get_api_columns
from flask_restful import Resource, reqparse, request


class ShipListAPI(Resource):
    def get(self):
        return get_json_data(Ship, get_api_columns(Ship), web_api=True)

    def post(self):
        pass


class ShipAPI(Resource):
    def __init__(self):
        self.parser = reqparse.RequestParser()
        colntype = get_api_columns(Ship, include_type=True)
        print(colntype)
        for col in colntype:
            self.parser.add_argument(col[0], type=col[1], location='json')
        # self.parser.add_argument('name', type=str, required=True,
        #                          help='No name specified', location='json')
        # self.parser.add_argument('code', type=str, default="", location='json')
        super(ShipAPI, self).__init__()

    def get(self, id):
        return get_json_data(Ship, get_api_columns(Ship), id, web_api=True)

    def put(self, id):
        data = dict(request.args)
        print(data)
        print('====================================')
        args = self.parser.parse_args()
        print(args)

    def delete(self, id):
        pass


class ShipTypeListAPI(Resource):
    def get(self):
        return get_json_data(ShipType, get_api_columns(Ship), web_api=True)

    def post(self):
        pass


class ShipTypeAPI(Resource):
    def get(self, id):
        return get_json_data(ShipType, get_api_columns(Ship), id, web_api=True)

    def put(self, id):
        pass

    def delete(self, id):
        pass


class ShipStatusListAPI(Resource):
    def get(self):
        return get_json_data(ShipStatus, get_api_columns(Ship), web_api=True)

    def post(self):
        pass


class ShipStatusAPI(Resource):
    def get(self, id):
        return get_json_data(ShipStatus, get_api_columns(Ship), id, web_api=True)

    def put(self, id):
        pass

    def delete(self, id):
        pass


class EngineListAPI(Resource):
    def get(self):
        return get_json_data(Engine, get_api_columns(Engine), web_api=True)

    def post(self):
        pass


class EngineAPI(Resource):
    def get(self, id):
        return get_json_data(Engine, get_api_columns(Engine), id, web_api=True)

    def put(self, id):
        pass

    def delete(self, id):
        pass


class BuilderListAPI(Resource):
    def get(self):
        return get_json_data(Builder, get_api_columns(Builder), web_api=True)

    def post(self):
        pass


class BuilderAPI(Resource):
    def get(self, id):
        return get_json_data(Builder, get_api_columns(Builder), id, web_api=True)

    def put(self, id):
        pass

    def delete(self, id):
        pass


api.add_resource(ShipListAPI, '/api/ships', endpoint='shiplist_api')
api.add_resource(ShipAPI, '/api/ships/<int:id>', endpoint='ship_api')
api.add_resource(EngineListAPI, '/api/engines', endpoint='enginelist_api')
api.add_resource(EngineAPI, '/api/engines/<int:id>', endpoint='engine_api')
api.add_resource(BuilderListAPI, '/api/builders', endpoint='builderlist_api')
api.add_resource(BuilderAPI, '/api/builders/<int:id>', endpoint='builder_api')
api.add_resource(ShipTypeListAPI, '/api/ship_types', endpoint='ship_typelist_api')
api.add_resource(ShipTypeAPI, '/api/ship_types/<int:id>', endpoint='ship_type_api')
api.add_resource(ShipStatusListAPI, '/api/ship_statuses', endpoint='ship_statuslist_api')
api.add_resource(ShipStatusAPI, '/api/ship_statuses/<int:id>', endpoint='ship_status_api')
print(__name__)
