from flask import Blueprint, redirect, render_template, request, url_for

from .. import supabase

auth = Blueprint(name="auth", import_name=__name__)


@auth.route("/login", methods=["GET", "POST"])
def login():
    msg = None
    if request.method == "POST":
        email = request.form.get("email")
        pswd = request.form.get("password")
        print(email, ' - ', pswd)
        try:
            user = supabase.auth.sign_in_with_password(
                {
                    "email": email,
                    "password": pswd,
                }
            )
            print("user logged in")
            return redirect("/user/dashboard")
        
        except:
            print("user create failed")
            return render_template("auth/login.html", msg=msg)
        
    return render_template("auth/login.html", msg=msg)


@auth.route("/logout")
def logout():
    res = supabase.auth.sign_out()
    return redirect(url_for("HomeViews.welcome_page"))


@auth.route("/signup", methods=["GET", "POST"])
def signup():
    if request.method == 'POST':
        email = request.form.get("email")
        pswd = request.form.get("password")
        print(email, ' - ', pswd)
        supabase.auth.sign_up(
            {
                "email": email,
                "password": pswd,
            }
        )
        print("user created")
        return redirect(url_for('UserViews.dashboard'))
    
    return render_template('auth/register.html')
