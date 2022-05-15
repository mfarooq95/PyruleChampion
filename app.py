from flask import Flask
from flask_restful import Api
from flask_bcrypt import Bcrypt
from flask_jwt_extended import JWTManager
import os
from database.db import initialize_db
from resources.routes import initialize_routes

app = Flask(__name__)
app.config.from_envvar('ENV_FILE')
api = Api(app)
bcrypt = Bcrypt(app)
jwt = JWTManager(app)

app.config['MONGODB_SETTINGS'] = {'host': 'mongodb://localhost/pyrulechampion'}

initialize_db(app)
initialize_routes(api)

app.run(debug = True)