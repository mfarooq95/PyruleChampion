from .pyrulechampion import OneHandedWeaponsAPI, OneHandedWeaponAPI
from .auth import SignupApi, LoginApi

def initialize_routes(api):
    api.add_resource(OneHandedWeaponsAPI, '/api/onehandedweapons')
    api.add_resource(OneHandedWeaponAPI, '/api/onehandedweapons/<id>') # Note the difference in resources passed and the endpoints in line 5 & 6
    api.add_resource(SignupApi, '/api/auth/signup')
    api.add_resource(LoginApi, '/api/auth/login')
