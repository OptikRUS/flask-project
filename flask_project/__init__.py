from flask import Flask
# from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager

# db = SQLAlchemy()
login_manager = LoginManager()


def create_app():
    app = Flask(__name__)

    login_manager.init_app(app)

    from flask_project.main.routes import main
    app.register_blueprint(main)

    return app
