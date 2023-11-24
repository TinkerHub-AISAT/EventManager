from flask import Blueprint

UserViews = Blueprint(name="UserViews", import_name=__name__)


@UserViews.route(rule="/profile", methods=["GET"])
def profile():
    return
