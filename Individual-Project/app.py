from flask import Flask, render_template, request, redirect, url_for, flash
from flask import session as login_session
import pyrebase

app = Flask(__name__, template_folder='templates', static_folder='static')
app.config['SECRET_KEY'] = 'super-secret-key'

#Code goes below here
config= {
  "apiKey": "AIzaSyCFZKBUpxUkdx3F1RLa1qcrfdZsmtzLwsQ",
  "authDomain": "first-shop-5af57.firebaseapp.com",
  "projectId": "first-shop-5af57",
  "storageBucket": "first-shop-5af57.appspot.com",
  "messagingSenderId": "866858112630",
  "appId": "1:866858112630:web:0589397f8c6c781efbb157",
  "measurementId": "G-E5ZDVMYLPY",
  "databaseURL": "https://first-shop-5af57-default-rtdb.europe-west1.firebasedatabase.app/"}
firebase = pyrebase.initialize_app(config)
auth = firebase.auth()
db = firebase.database()

@app.route('/', methods=['GET', 'POST'])
def HOME():
    return render_template("Home.html")

@app.route('/store', methods=['GET', 'POST'])
def LOGIN():
    return render_template("Store.html")

#Code goes above here

if __name__ == '__main__':
    app.run(debug=True)