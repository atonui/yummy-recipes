"""Start the server"""
from app.users import Users, USERLIST

from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/login/')
def login():
    return render_template("login.html")

@app.route("/signupsuccess", methods=['POST'])
def dashboard():
    if request.method == 'POST':
        email = request.form["email_name"]
        password = request.form["password"]
        user = Users(object)
        if user.fetch_user(email, password) is True:
            return render_template("login.html")
        else:
            user.add_user(email, password)
            print(USERLIST)
            return render_template ("dashboard.html")

@app.route("/loginsuccess", methods = ['POST'])
def loginsuccess():
    if request.method == 'POST':
        email = request.form["email_name"]
        password = request.form["password"]
        user = Users(object)
        if fetch_user(email, password) is True:
            render_template ("dashboard.html")

@app.route('/signup/')
def signup():
    return render_template("signup.html")

if __name__ == '__main__':
    app.run(debug=True)
