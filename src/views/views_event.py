from flask import Blueprint, render_template

from ..models import models_crud

ViewEvent = Blueprint(name="ViewsEvent", import_name=__name__)


@ViewEvent.route(rule="/eventplace", methods=["GET"])
def eventplace():
    event_list = models_crud.event_fetch_all()
    print(event_list)
    return render_template(
        template_name_or_list="event/event_eventplace.html",
        event_list=event_list,
    )


@ViewEvent.route(rule="/update", methods=["GET"])
def update():
    return render_template(template_name_or_list="event/event_update.html")


@ViewEvent.route(rule="/create", methods=["GET"])
def create():
    return render_template(template_name_or_list="event/event_create.html")
