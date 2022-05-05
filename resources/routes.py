# Local imports -- Flask RESTFUL Resources
from .pyrulechampion import OneHandedWeaponsAPI, OneHandedWeaponAPI
from .auth import SignupApi, LoginApi

# Function to initiliaze flask routes, passing in <api> as a requirement for when function is called
def initialize_routes(api):
    # Utilizing the <api> variable, which houses the Api(app) object from flask_restful instantiated in app.py, use the <.add_resource()> method to pass resources defined and the endpoint
    api.add_resource(OneHandedWeaponsAPI, '/api/onehandedweapons')
    api.add_resource(OneHandedWeaponAPI, '/api/onehandedweapons/<id>') # Note the difference in resources passed and the endpoints in line 8 & 9
    api.add_resource(SignupApi, '/api/auth/signup')
    api.add_resource(LoginApi, '/api/auth/login')