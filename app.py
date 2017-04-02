from flask import (Flask, g, render_template, flash, redirect, url_for)
from flask_bcrypt import check_password_hash
from flask_login import LoginManager, login_user

import forms
import models

DEBUG = True
PORT = 8000
HOST = '0.0.0.0'

flaskApp = Flask(__name__)
flaskApp.secret_key = "aojsdfonzsdofewutoutaoijnoe!igaosudg9ongoansgoiag"

loginManager = LoginManager()
loginManager.init_app(flaskApp)
loginManager.login_view = "login"

@flaskApp.before_request
def beforeRequest():
    """Connect to the database before each request"""
    g.db = models.DATABASE
    g.db.connect()

@flaskApp.after_request
def afterRequest(response):
    """Close the database connection after each request"""
    g.db.close()
    return response

@flaskApp.route('/register', methods=('GET', 'POST'))
def register():
    form = forms.RegisterForm()
    if form.validate_on_submit():
        flash("Yay, you registered!", "success")
        models.User.createUser(
            username=form.username.data,
            email=form.email.data,
            password=form.password.data
            )
        return redirect(url_for('index'))
    return render_template('register.html',form=form)

@flaskApp.route('/login', methods=('GET', 'POST'))
def login():
    form = forms.LoginForm()
    if form.validate_on_submit():
        try:
            user = models.User.get(models.User.email == form.email.data)
        except models.DoesNotExist:
            flash("Your email or password doesn't match!", "error")
        else:
            if check_password_hash(user.password, form.password.data):
                login_user(user)
                flash("You've been logged in!", "success")
                return redirect(url_for('index'))
            else:
                flash("Your email or password doesn't match!", "error")
    return render_template('login.html', form=form)

@flaskApp.route('/', methods=['GET'])
def index():
    return "Hi"


@loginManager.user_loader
def load_user(userid):
    try:
        return models.User.get(models.User.id == userid)
    except models.DoesNotExist:
        return None

if __name__ == "__main__":
    models.initialize()
    try:
        models.User.createUser(
            username= 'dtonlai',
            email = 'dtonlai@ualberta.ca',
            password='password',
            admin= True,
            )
    except ValueError:
        pass
    flaskApp.run(debug= DEBUG,port= PORT,host= HOST)

