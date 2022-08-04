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
def home():
    if 'user' in login_session:
        if None != login_session['user']:
            print(login_session)
            x=db.child("Users").child(login_session['user']['localId']).child('username').get().val()
            return render_template("home.html",x=x)
    return redirect(url_for('login'))

@app.route('/popstore', methods=['GET', 'POST'])
def POP():
    return render_template("POP.html")

@app.route('/rockstore', methods=['GET', 'POST'])
def Rock():
    return render_template("Rock.html")

@app.route('/jazzstore', methods=['GET', 'POST'])
def Jazz():
    return render_template("Jazz.html")

@app.route('/cart', methods=['GET', 'POST'])
def cart():
    return render_template("cart.html")

@app.route('/countrystore', methods=['GET', 'POST'])
def Country():
    return render_template("country.html")

@app.route('/login', methods=['GET', 'POST'])
def login():
    error = ""

    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']
        try:
            login_session['user'] = auth.sign_in_with_email_and_password(email, password)
            return redirect(url_for('home'))
        except:
            error = "Authentication failed"
            return error
    else:
        return render_template("login.html")

@app.route('/signup', methods=['GET', 'POST'])
def signup():
    if request.method == 'POST':
        try:
            email = request.form['email']
            password = request.form['password']
            login_session['user'] = auth.create_user_with_email_and_password(email, password)
            user = {"email":request.form["email"], "password":request.form["password"] ,"username":request.form["username"]}
            db.child("Users").child(login_session['user']['localId']).set(user)
            return redirect(url_for('home'))
        except:
            error = "Authentication failed"
            return (error)
    else:
        return render_template("signup.html")

@app.route('/logout', methods=['GET', 'POST'])
def logout():
    login_session['user'] = None
    auth.current_user = None
    return redirect(url_for('login'))


#Code goes above here

if __name__ == '__main__':
    app.run(debug=True)