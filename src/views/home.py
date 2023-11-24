from flask import Blueprint, render_template

home_views = Blueprint(name="home_views", import_name=__name__)


@home_views.route(rule="/", methods=["GET"])
def welcome_page():
    return render_template("home/home_welcome.html")


@home_views.route(rule="/aboutus", methods=["GET"])
def aboutus():
    return render_template("home/home_about.html")


@home_views.route(rule="/contactus", methods=["GET"])
def contactus():
    return render_template("home/home_contact.html")
