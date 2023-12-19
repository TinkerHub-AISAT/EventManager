from flask import Blueprint, render_template

from ..models import models_crud

UserViews = Blueprint(name="UserViews", import_name=__name__)


@UserViews.route(rule="/profile", methods=["GET"])
def profile():
    return render_template(template_name_or_list="user/user_profile.html")


@UserViews.route(rule="/dashboard", methods=["GET"])
def dashboard():
    event_list = models_crud.event_fetch_all()
    return render_template(
        template_name_or_list="user/user_dashboard.html", event_list=event_list
    )


@UserViews.route(rule="/settings", methods=["GET"])
def settings():
    return render_template(template_name_or_list="user/user_settings.html")
