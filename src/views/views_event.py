from flask import Blueprint, redirect, render_template, request, url_for

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


@ViewEvent.route(rule="/update", methods=["GET", "POST"])
def update(event_id: str):
    if request.method == "POST":
        pass
    else:
        event_data = models_crud.event_fetch_by_id(event_id=event_id)
        return render_template(
            template_name_or_list="event/event_update.html",
            event_data=event_data,
        )


@ViewEvent.route(rule="/create", methods=["GET"])
def create():
    if request.method == "POST":
        data = {}

        models_crud.event_create(event_data=data)

        return redirect(location=url_for(endpoint="ViewEvent.eventplace"))
    else:
        return render_template(template_name_or_list="event/event_create.html")
