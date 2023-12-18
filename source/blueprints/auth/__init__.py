from flask import Blueprint

auth_blueprint = Blueprint('auth', __name__,  static_folder='static', static_url_path='/auth/static' ,template_folder='templates')

from . import views
