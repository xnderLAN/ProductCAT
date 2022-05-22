from flask import Flask
from flask_mongoengine import MongoEngine, Document
from flask_login import LoginManager
import pymongo


db = MongoEngine()
login_manager = LoginManager()

def create_app():
    app = Flask(__name__)
    app.config["MONGODB_SETTINGS"] = {
        'db': 'ProductCAT',
        'host': 'localhost'
    }
    db.init_app(app)
    app.config["SECRET_KEY"] = "ALPSOODKEdkhfds4d5s6f4dsfALPSOODKEdkhfds4d5s6f4dsf"
    login_manager.init_app(app)
    login_manager.login_view = 'login'
    
    from .views import views
    app.register_blueprint(views)
    from .auth import auth
    app.register_blueprint(auth)
    
    return app, db, login_manager


app, _, _ = create_app()

