from flask import Blueprint, redirect, render_template, url_for

from .. import supabase
from ..models import models_crud

UserViews = Blueprint(name="UserViews", import_name=__name__)


@UserViews.route(rule="/profile", methods=["GET"])
def profile():
    return render_template(template_name_or_list="user/user_profile.html")


@UserViews.route(rule="/dashboard", methods=["GET"])
def dashboard():
    session = supabase.auth.get_user()
    if session is None:
        return redirect(location=url_for(endpoint="auth.login"))

    event_list = models_crud.event_fetch_all()
    return render_template(
        template_name_or_list="user/user_dashboard.html",
        event_list=event_list,
        user=session.user.id,
    )


@UserViews.route(rule="/register", methods=["POST"])
def register(event_id: int):
    session = supabase.auth.get_user()
    if session is None:
        return redirect(location=url_for(endpoint="auth.login"))
    return render_template(template_name_or_list="user/user_dashboard.html")


@UserViews.route(rule="/unregister", methods=["POST"])
def unregister(id: int):
    session = supabase.auth.get_user()
    if session is None:
        return redirect(location=url_for(endpoint="auth.login"))
    return render_template(template_name_or_list="user/user_dashboard.html")


@UserViews.route(rule="/settings", methods=["GET"])
def settings():
    session = supabase.auth.get_user()
    if session is None:
        return redirect(location=url_for(endpoint="auth.login"))
    return render_template(template_name_or_list="user/user_settings.html")
