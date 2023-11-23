from flask import Blueprint, render_template

home_views = Blueprint("home_views", __name__)


@home_views.route("/")
def welcome_page():
    return render_template("home/home_welcome.html")


@home_views.route("/aboutus")
def aboutus():
    return render_template("home/home_about.html")


@home_views.route("/contactus")
def contactus():
    return render_template("home/home_contact.html")
