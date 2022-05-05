# Import external packages
from flask import Flask
from flask_restful import Api
from flask_bcrypt import Bcrypt
from flask_jwt_extended import JWTManager

# Local imports -- Functions, database models, and routes
from database.db import initialize_db
from resources.routes import initialize_routes

# Instantiate Flask application/object
app = Flask(__name__)

# Configure Flask to use env variable from .env file and location
pass

# Instantiate Api object from flask_restful -- pass in Flask application <app>
api = Api(app)

# Instantiate Bcrypt object from flask_bcrypt -- pass in Flask application <app>
bcrypt = Bcrypt(app)

# Instantiate JWTManager object from flask_jwt_extended -- pass in Flask application <app>
jwt = JWTManager(app)

# Congiure Flask app to use specified MongoDB settings -- can be more specific in dict
app.config['MONGODB_SETTINGS'] = {
    'host': 'mongodb://localhost/pyrulechampion'
    }

# Call and run functions to initialize database and routes -- functions locally imported from .py files and take one arguement, the Flask app <app>, to be passed into them
initialize_db(app)
initialize_routes(api)

# Run Flask app -- debug:parameter set to True during development only
app.run(debug = True)