# blueprints/profiles/views.py
from flask import render_template
from . import profiles_blueprint
import os
import toml

# SESSION_PATH = os.path.join(os.path.dirname(os.path.dirname(os.path.dirname(__file__))), "sessions")

@profiles_blueprint.route("/index/<session_name>/profile/<int:profile_id>")
def display_profile(session_name, profile_id):
    # Use session_name to locate the correct directory
    profile_path = os.path.join("source/sessions", session_name, "profiles")
    profile_file = os.path.join(profile_path, f"person_{profile_id}.toml")
    picture_file = f"profile_pictures/profilepicture_{profile_id}.png" # Update for static directory
    with open(profile_file, "r", encoding="utf8") as f:
        text = f.read()
        person = toml.loads(text)
    return render_template(
        "profiles/display_profile.html",
        person=person,
        picture_file=picture_file, # Static directory reference
        profile_id=str(profile_id),
        session_name=session_name,
    )