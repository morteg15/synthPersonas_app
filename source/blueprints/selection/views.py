from flask import render_template
from . import selection_blueprint
import os

SESSION_PATH = 'source/sessions'

@selection_blueprint.route('/selection')
def selection():
    sessions = [
    s
    for s in os.listdir(SESSION_PATH)
    if os.path.isdir(os.path.join(SESSION_PATH, s))
    ]
    if not sessions:
        return render_template('selection/selection.html', sessions=None)
    else:
        return render_template('selection/selection.html', sessions=sessions)



