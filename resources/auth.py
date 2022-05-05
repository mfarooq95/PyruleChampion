# Import external packages
from flask import request
from flask_restful import Resource

# Local imports -- User class model for document schema
from database.models import User

# Flask RESTFUL Resource for working with users who wants to sign up and add documents into the collection
class SignupApi(Resource):
    def post(self):
        body = request.get_json()
        user = User(**body)
        user.hash_password()
        user.save()
        id = user.id
        return {'id': str(id)}, 200

# Flask RESTFUL Resource for working with users who have "accounts" and want to sign in to work with documents in collections
class LoginApi(Resource):
    def post(self):
        body = request.get_json()
        user = User.objects.get(email = body.get('email'))
        authorized = user.check_password(body.get('password'))
        if not authorized:
            return {'error': 'Email or password invalid'}, 401
        
        expires = datetime.timedelta(days = 7)
        access_token = create_access_token(identity = str(user.id), expires_delta = expires)
        return {'token': access_token}, 200
