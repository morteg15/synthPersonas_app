from flask import Blueprint

selection_blueprint = Blueprint(
    "selection",
    __name__,
    static_folder="static",
    static_url_path="/selection/static",
    template_folder="templates",
)

from . import views
