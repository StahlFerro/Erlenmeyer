from pprint import pprint
from datetime import timedelta

from flask_restful import Resource, request
from flask_jwt_extended import jwt_required, jwt_refresh_token_required, get_jwt_identity, get_raw_jwt

from server import api
from server.models import Ship, ShipType, ShipStatus, Engine, Builder, User, RevokedToken
from server.utils.transaction import get_records, create_records, update_records, delete_record
# from server.utils.token import user_from_secret, reset_client_secret, generate_access_token, generate_refresh_token


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
        self.model = Builder

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


class UserDebugAPI(Resource):
    def get(self, id):
        user = User.query.get(id)
        access_token = user.generate_access_token()
        refresh_token = user.generate_refresh_token()
        if not user:
            return {"msg": "User not found"}, 404
        return {
            "access_token": access_token,
            "refresh_token": refresh_token,
        }, 200

    @jwt_required
    def post(self, id):
        user = User.from_secret(get_jwt_identity())
        if user:
            return {"identity": user.client_secret, "username": user.username}, 200
        else:
            return {"msg": "Token has expired"}, 401

    @jwt_refresh_token_required
    def put(self, id):
        user = User.from_secret(get_jwt_identity())
        if not user:
            return {"msg": "Token has expired"}, 401

        jti = get_raw_jwt()['jti']
        old_token = RevokedToken(jti=jti)
        old_token.add()

        new_token = user.generate_access_token()
        return {"access_token": new_token}, 200

    @jwt_refresh_token_required
    def delete(self, id):
        user = User.from_secret(get_jwt_identity())
        if not user:
            return {"msg": "Token has expired"}, 401
        user.reset_client_secret()
        pprint(get_raw_jwt())
        jti = get_raw_jwt()['jti']
        revoked_token = RevokedToken(jti=jti)
        revoked_token.add()
        return {"message": "Client secret reset, all access and refresh tokens invalidated"}, 200


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
api.add_resource(UserDebugAPI, '/api/users/debug/<int:id>', endpoint='users_debug_api')
print(__name__)
