from flask import Flask


def flask_app():
    app = Flask(__name__)

    from .views import home

    app.register_blueprint(home.home_views, url_prefix="/")

    return app
