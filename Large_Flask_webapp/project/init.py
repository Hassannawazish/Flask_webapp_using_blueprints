from flask import Flask
from flask_login import LoginManager
import secrets
import os, setproctitle, logging
from database.setup import init_db

login_manager = LoginManager()

app = Flask(__name__)
app.secret_key = secrets.token_urlsafe(16)

init_db()

login_manager.init_app(app)
login_manager.login_view = "login"

from project.register.views import registeration_blueprint
from project.suggestions.views import suggestion_blueprint

app.register_blueprint(registeration_blueprint, url_prefix="/register")
app.register_blueprint(suggestion_blueprint, url_prefix="/suggest")
