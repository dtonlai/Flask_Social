from flask import Flask, g
from flask_login import LoginManager

import models

DEBUG = True
PORT = 8000
HOST = '0.0.0.0'

flaskApp = Flask(__name__)
flaskApp.secret_key = "aojsdfonzsdofewutoutaoijnoe!igaosudg9ongoansgoiag"

@flaskApp.before_request
def beforeRequest():
	"""Connect to the database before each request"""
	g.db = models.database
	g.db.connnect()

@flaskApp.after_request
def afterRequest(response):
	"""Close the database connection after each request"""
	g.db.close()
	return response

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

