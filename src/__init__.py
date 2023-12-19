from flask import Flask
from supabase import Client, create_client

from .config import cred

supabase: Client = create_client(
    supabase_url=cred.supabase_url(), supabase_key=cred.supabase_key()
)


def flask_app() -> Flask:
    app = Flask(import_name=__name__)
    app.config["SECRET_KEY"] = "hjshjhdjah kjshkjdhjs"

    from .auth import auth_user
    from .views import views_event, views_home, views_user

    app.register_blueprint(blueprint=views_home.HomeViews, url_prefix="/")
    app.register_blueprint(blueprint=views_user.UserViews, url_prefix="/user")
    app.register_blueprint(blueprint=views_event.ViewEvent, url_prefix="/event")
    app.register_blueprint(blueprint=auth_user.auth, url_prefix="/auth")

    return app
