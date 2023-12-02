from flask import Blueprint, redirect, render_template, request

from .. import supabase

auth = Blueprint(name="auth", import_name=__name__)


@auth.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        email = request.form.get("email")
        pswd = request.form.get("password")
        try:
            user = supabase.auth.sign_in_with_password(
                {
                    "email": email,
                    "password": pswd,
                }
            )
            return redirect("/user/")
        except:
            return render_template("", user=user)

    return render_template("", user=user)


@auth.route("/logout")
def logout():
    res = supabase.auth.sign_out()
    return redirect("/")


@auth.route("/signup", methods=["GET", "POST"])
def signup():
    email = ""
    pswd = ""
    supabase.auth.sign_up(
        {
            "email": email,
            "password": pswd,
        }
    )
    return render_template()
