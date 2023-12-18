from flask import Flask, redirect, url_for, session

# Blueprint imports
from blueprints.auth import auth_blueprint
from blueprints.selection import selection_blueprint
from blueprints.session import session_blueprint
from blueprints.profiles import profiles_blueprint

# Other blueprint imports...


def create_app():
    app = Flask(__name__)
    # secret key for session
    secret_key = "secret_key"
    app.secret_key = secret_key


    # Register Blueprints
    app.register_blueprint(auth_blueprint, url_prefix="/auth")
    app.register_blueprint(selection_blueprint, url_prefix="/selection")
    app.register_blueprint(session_blueprint, url_prefix="/session")
    app.register_blueprint(profiles_blueprint, url_prefix="/profiles")

    @app.route("/")
    def index():
        # read cfg file check api_key_set if true then redirect to main page
        app.config.from_pyfile("config.cfg")
        if app.config["API_KEY_SET"]:
            session["api_key"] = app.config["API_KEY"]
            return redirect(
                url_for("selection.selection")
            ) 
        return redirect(
            url_for("auth.get_api_key")
        ) 
    return app


if __name__ == "__main__":
    app = create_app()
    app.run(debug=True)
