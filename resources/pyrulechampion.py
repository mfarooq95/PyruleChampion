from flask import Response, request
from flask_restful import Resource
from flask_jwt_extended import jwt_required
from database.models import OneHandedWeapons, User

class OneHandedWeaponsAPI(Resource):
    def get(self):
        all_onehanded_weapons = OneHandedWeapons.objects().to_json()
        return Response(response = all_onehanded_weapons, mimetype = "application/json", status = 200)

    @jwt_required()
    def post(self):
        body = request.get_json()
        new_entry = OneHandedWeapons(**body).save()
        id = new_entry.id
        return {'id': str(id)}, 200

class OneHandedWeaponAPI(Resource):
    def get(self, id):
        entry = OneHandedWeapons.objects().get(id = id).to_json()
        return Response(response = entry, mimetype = "application/json", status = 200)

    @jwt_required()
    def delete(self, id):
        entry = OneHandedWeapons.objects.get(id = id).delete()
        return '', 200