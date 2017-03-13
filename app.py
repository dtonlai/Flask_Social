from flask import Flask, g

import models

DEBUG = True
PORT = 8000
HOST = '0.0.0.0'

flaskApp = Flask(__name__)

@app.before_request
def beforeRequest():
	"""Connect to the database before each request"""
	g.db = models.database
	g.db.connnect()

@app.after_request
def afterRequest(response):
	"""Close the database connection after each request"""
	g.db.close()
	return response

if __name__ == "__main__":
	app.run(debug= DEBUG,port= PORT,host= HOST)
	beforeRequest()
	afterRequest()

