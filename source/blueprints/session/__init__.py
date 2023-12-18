from flask import Blueprint

session_blueprint = Blueprint(
    "session",
    __name__,
    static_folder="static",
    static_url_path="/session/static",
    template_folder="templates",
)

from . import views
