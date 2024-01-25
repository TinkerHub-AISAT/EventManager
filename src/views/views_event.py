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


@ViewEvent.route(rule="/update/", methods=["GET"])
def update(event_id: str):
    if request.method == "POST":
        event_title: str = request.form.get(key="event_title")
        event_description: str = request.form.get(key="event_description")
        event_date: str = request.form.get(key="event_date")
        event_time: str = request.form.get(key="event_time")
        event_location: str = request.form.get(key="event_location")
        data: dict[str, str] = {
            "event_title": event_title,
            "event_desc": event_description,
            "event_date": event_date,
            "event_time": event_time,
            "event_location": event_location,
        }

        models_crud.event_update(event_id=event_id, data=data)
        return redirect(location=url_for(endpoint="UserViews.profile"))

    else:
        event_data = models_crud.event_fetch_by_id(event_id=event_id)
        return render_template(
            template_name_or_list="event/event_update.html",
            event_data=event_data,
        )


@ViewEvent.route(rule="/create", methods=["GET", "POST"])
def create():
    if request.method == "POST":
        # inputs
        event_title: str = request.form.get(key="event_title")
        event_description: str = request.form.get(key="event_description")
        event_date: str = request.form.get(key="event_date")
        event_time: str = request.form.get(key="event_time")
        event_location: str = request.form.get(key="event_location")
        event_particient: int = 0

        # data dict
        data: dict[str, str] = {
            "event_title": event_title,
            "event_desc": event_description,
            "event_date": event_date,
            "event_time": event_time,
            "event_location": event_location,
            "event_particient": event_particient,
            "created_by": "admin",
        }

        # update the event data
        models_crud.event_create(event_data=data)
        return redirect(location=url_for(endpoint="UserViews.profile"))

    else:
        return render_template(template_name_or_list="event/event_create.html")

@ViewEvent.route(rule="/delete/<event_id>", methods=["GET"])
def delete(event_id: str):
    return render_template()