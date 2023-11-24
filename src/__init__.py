# * Dotenv module
from dotenv import load_dotenv
from flask import Flask

# * firebase admin
# import firebase_admin
# from firebase_admin import credentials, firestore


# custom imports
# from .config.cred import FirebaseCreds

# load of the env variables in the project environment
load_dotenv()


def flask_app():
    app = Flask(import_name=__name__)

    # _FIREBASECRED = FirebaseCreds()

    from .views import views_home, views_user

    app.register_blueprint(blueprint=views_home.HomeViews, url_prefix="/")
    app.register_blueprint(blueprint=views_user.UserViews, url_prefix="/user")

    return app
