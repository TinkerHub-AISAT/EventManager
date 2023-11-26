from flask import Blueprint, render_template

UserViews = Blueprint(name="UserViews", import_name=__name__)


@UserViews.route(rule="/profile", methods=["GET"])
def profile():
    return render_template("user/user_profile.html")


@UserViews.route(rule="/dashboard", methods=["GET"])
def dashboard():
    return render_template("user/user_dashboard.html")


@UserViews.route(rule="/settings", methods=["GET"])
def settings():
    return render_template("user/user_settings.html")
