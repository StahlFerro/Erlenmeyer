from server import app, api
from server.models import Ship, Engine, get_json_data, get_api_columns
from flask_restful import Resource


class ShipListAPI(Resource):
    def get(self):
        return get_json_data(Ship, get_api_columns(Ship))

    def post(self):
        pass


class ShipAPI(Resource):
    def get(self, id):
        return get_json_data(Ship, get_api_columns(Ship), id)

    def put(self, id):
        pass

    def delete(self, id):
        pass

class EngineListAPI(Resource):
    def get(self):
        return get_json_data(Engine, get_api_columns(Engine))

    def post(self):
        pass


class EngineAPI(Resource):
    def get(self, id):
        return get_json_data(Engine, get_api_columns(Engine), id)

    def put(self, id):
        pass

    def delete(self, id):
        pass

api.add_resource(ShipListAPI, '/api/ships', endpoint='shiplist_api')
api.add_resource(ShipAPI, '/api/ships/<int:id>', endpoint='ship_api')
api.add_resource(EngineListAPI, '/api/engines', endpoint='enginelist_api')
api.add_resource(EngineAPI, '/api/engines/<int:id>', endpoint='engine_api')
print(__name__)
