# Import external packages
from flask_mongoengine import MongoEngine

# Instantiated MongoEngine object; stored into variable
db = MongoEngine()

# Function to initialize database with Flask app by passing in <app> as a requirement for when function is called
def initialize_db(app):
    # Utilizes a MonogEngine() method <.init_app()> and pass it the required <app> arguement which is the Flask app which is present in app.py, where this function will be called
    db.init_app(app)