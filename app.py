from flask import (Flask, g, render_template, flash, redirect, url_for)
from flask_login import LoginManager

import forms
import models

DEBUG = True
PORT = 8000
HOST = '0.0.0.0'

flaskApp = Flask(__name__)
flaskApp.secret_key = "aojsdfonzsdofewutoutaoijnoe!igaosudg9ongoansgoiag"

@flaskApp.before_request
def beforeRequest():
	"""Connect to the database before each request"""
	g.db = models.DATABASE
	g.db.connnect()

@flaskApp.after_request
def afterRequest(response):
	"""Close the database connection after each request"""
	g.db.close()
	return response

@app.route('/register', methods('GET', 'POST'))
def register():
	form = forms.RegisterForm()
	if form.validate_on_submit():
		flash("Yay, you registered!", "success")
		model.User.createUser(
			username=form.username.data,
			email=form.email.data,
			password=form.password.data
			)
		return redirect(url_for('index'))
	return render_template('register.html',form=form)

@app.route('/', methods('GET'))
def index():
	return "Hi"

loginManager = LoginManager()
loginManager.init_app(flaskApp)
loginManager.login_view = "login"

@login_manager.user_loader
def load_user(userid):
	try:
		return models.User.get(models.User.id == userid)
	except models.DoesNotExist:
		return None

if __name__ == "__main__":
	models.initialize()
	models.User.create_user(
		name= 'dtonlai',
		email = 'dtonlai@ualberta.ca',
		password='password',
		admmin= True,
		)
	app.run(debug= DEBUG,port= PORT,host= HOST)

