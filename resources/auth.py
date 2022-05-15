from flask import Response, request
from flask_restful import Resource
from flask_jwt_extended import create_access_token
import datetime
from database.models import User

class SignupApi(Resource):
    def post(self):
        body = request.get_json()
        user = User(**body)
        user.hash_password()
        user.save()
        id = user.id
        return {'id': str(id)}, 200

class LoginApi(Resource):
    def post(self):
        body = request.get_json()
        user = User.objects.get(email = body.get('email'))
        authorized = user.check_password(password = body.get('password'))
        if not authorized:
            return {'error': 'Email or password invalid'}, 401
        
        expiration = datetime.timedelta(days = 7)
        access_token = create_access_token(identity = str(user.id), expires_delta = expiration)
        return {'token': access_token}, 200
