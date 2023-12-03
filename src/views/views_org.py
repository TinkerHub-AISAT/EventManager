from flask import Blueprint, render_template

ViewsOrg = Blueprint(name="ViewsOrg", import_name=__name__)


@ViewsOrg.route(rule="/profile", methods=["GET"])
def profile():
    return render_template(template_name_or_list="user/user_profile.html")


@ViewsOrg.route(rule="/dashboard", methods=["GET"])
def dashboard():
    return render_template(template_name_or_list="user/user_dashboard.html")


@ViewsOrg.route(rule="/settings", methods=["GET"])
def settings():
    return render_template(template_name_or_list="user/user_settings.html")
