from flask import Flask, flash, render_template, session, redirect, request, url_for
from flask_login import LoginManager
from models import User
from datetime import *
import os

app = Flask(__name__)
app.config["SECRET_KEY"] = "courseLastTermPaw123"
app.config["UPLOAD_FOLDER"] = os.path.realpath('.') + '/static/uploads'
app.config["MAX_CONTENT_PATH"] = 20000000
app.permanent_session_lifetime = timedelta(hours=3)

login_manager = LoginManager()
login_manager.init_app(app)

@login_manager.user_loader
def load_user(id, endpoint='user'):
	if endpoint == 'user':
		User.openDB()
		data = cursor.execute("SELECT idUser from user where idUser='{0}'".format(id))
		return data