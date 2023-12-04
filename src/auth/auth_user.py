from flask import Blueprint, flash, redirect, render_template, request, url_for
from gotrue.errors import AuthApiError

from .. import supabase

auth = Blueprint(name="auth", import_name=__name__)


@auth.route(rule="/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        email: str = request.form.get(key="email")
        pswd: str = request.form.get(key="password")

        if len(pswd) < 8:
            flash(
                message="Enter a vaild password atleast 8 characters long",
                category="error",
            )

        elif len(email) < 5:
            flash(message="Enter a vaild email", category="error")

        else:
            try:
                seesion = supabase.auth.sign_in_with_password(
                    credentials={"email": email, "password": pswd}
                )
                flash(message=f"Logged in !!", category="success")
                return redirect(location=url_for(endpoint="UserViews.dashboard"))

            except AuthApiError:
                flash(message="Invaild credentials", category="error")
                return render_template(template_name_or_list="auth/login.html")

    return render_template(template_name_or_list="auth/login.html")


@auth.route(rule="/logout")
def logout():
    supabase.auth.sign_out()
    flash(message="Logged out !!", category="success")
    return redirect(location=url_for(endpoint="HomeViews.welcome_page"))


@auth.route(rule="/signup", methods=["GET", "POST"])
def signup():
    if request.method == "POST":
        email: str = request.form.get(key="email")
        pswd: str = request.form.get(key="password")
        pswd_confirm: str = request.form.get(key="confirm")

        if len(pswd) < 8:
            flash(
                message="Enter a vaild password atleast 8 characters long",
                category="error",
            )
        elif pswd == pswd_confirm:
            flash(message="Passwors doesn't match", category="error")
        elif len(email) < 5:
            flash(message="Enter a vaild email", category="error")
        else:
            session = supabase.auth.sign_up(
                credentials={"email": email, "password": pswd}
            )

            flash(message=f"Account created ", category="success")
            return redirect(location=url_for(endpoint="UserViews.dashboard"))

    return render_template(template_name_or_list="auth/register.html")
