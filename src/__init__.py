import firebase_admin
from firebase_admin import credentials, firestore
from flask import Flask

# custom imports
from .config.cred import FirebaseCreds

# ? Firebase config
# Load Firebase credentials
firebase_creds = FirebaseCreds()

# Convert FirebaseCreds to a dictionary
firebase_creds_dict = firebase_creds.to_json()

# Create a Firebase credentials object
cred = credentials.Certificate(firebase_creds_dict)

# Initialize Firebase app
firebase_admin.initialize_app(cred)

db = firestore.client()


def flask_app():
    app = Flask(import_name=__name__)

    from .views import views_event, views_home, views_user

    app.register_blueprint(blueprint=views_home.HomeViews, url_prefix="/")
    app.register_blueprint(blueprint=views_user.UserViews, url_prefix="/user")
    app.register_blueprint(blueprint=views_event.ViewEvent, url_prefix="/event")

    return app
