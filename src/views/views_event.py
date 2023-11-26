from flask import Blueprint, render_template

ViewEvent = Blueprint(name="ViewsEvent", import_name=__name__)


@ViewEvent.route("/eventplace", methods=["GET"])
def eventplace():
    return render_template("event/event_eventplace.html")


@ViewEvent.route("/update", methods=["GET"])
def update():
    return render_template("event/event_update.html")


@ViewEvent.route("/create", methods=["GET"])
def create():
    return render_template("event/event_create.html")
