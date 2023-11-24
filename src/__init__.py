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
    app = Flask(__name__)

    # _FIREBASECRED = FirebaseCreds()

    from .views import home

    app.register_blueprint(home.home_views, url_prefix="/")

    return app
