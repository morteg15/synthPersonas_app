from flask import Blueprint

profiles_blueprint = Blueprint('profiles', __name__,  static_folder='static', static_url_path='/profiles/static' ,template_folder='templates')

from . import views
