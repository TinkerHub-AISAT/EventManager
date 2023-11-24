from flask import Blueprint, render_template

HomeViews = Blueprint(name="HomeViews", import_name=__name__)


@HomeViews.route(rule="/", methods=["GET"])
def welcome_page():
    return render_template("home/home_welcome.html")


@HomeViews.route(rule="/aboutus", methods=["GET"])
def aboutus():
    return render_template("home/home_about.html")


@HomeViews.route(rule="/contactus", methods=["GET"])
def contactus():
    return render_template("home/home_contact.html")
