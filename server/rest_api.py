from server import app, api
from server.models import Ship, ShipType, ShipStatus, Engine, Builder, get_json_data, get_api_columns
from flask_restful import Resource


class ShipListAPI(Resource):
    def get(self):
        return get_json_data(Ship, get_api_columns(Ship), web_api=True)

    def post(self):
        pass


class ShipAPI(Resource):
    def get(self, id):
        return get_json_data(Ship, get_api_columns(Ship), id, web_api=True)

    def put(self, id):
        pass

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


api.add_resource(ShipListAPI, '/api/ship', endpoint='shiplist_api')
api.add_resource(ShipAPI, '/api/ship/<int:id>', endpoint='ship_api')
api.add_resource(EngineListAPI, '/api/engine', endpoint='enginelist_api')
api.add_resource(EngineAPI, '/api/engine/<int:id>', endpoint='engine_api')
api.add_resource(BuilderListAPI, '/api/builder', endpoint='builderlist_api')
api.add_resource(BuilderAPI, '/api/builder/<int:id>', endpoint='builder_api')
api.add_resource(ShipTypeListAPI, '/api/ship_type', endpoint='ship_typelist_api')
api.add_resource(ShipTypeAPI, '/api/ship_type/<int:id>', endpoint='ship_type_api')
api.add_resource(ShipStatusListAPI, '/api/ship_status', endpoint='ship_statuslist_api')
api.add_resource(ShipStatusAPI, '/api/ship_status/<int:id>', endpoint='ship_status_api')
print(__name__)
