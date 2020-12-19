from flask import *
import os

app = Flask(__name__)

app.secret_key = os.urandom(32)

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/login/')
def login():
    return render_template("login.html")

@app.route('/profile/', methods=["GET", "POST"])
def profile():

    if request.method == 'POST':
        session['email'] = request.form['email']
        session['username'] = request.form['username']

    if 'email' and 'username' in session:  
        email = session['email']
        username = session['username']
        #password = session['password'] 
    return render_template("profile.html", name = username, mail = email)

@app.route('/logout/')
def logout():
    session.pop('username', None)
    session.pop('email', None)
    return render_template("logout.html")