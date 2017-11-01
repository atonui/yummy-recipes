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
def signupsuccess():
    if request.method == 'POST':
        email = request.form["email_name"]
        password = request.form["password"]
        username = request.form["username"]
        name = request.form["name"]
        user = Users(email, password, username, name)
        if user.fetch_user(email, password) is True:
            print("This is the full userlist",USERLIST)
            return render_template("signup.html", text="That user already exists.")
        else:
            user.add_user(email,password,username,name)
            return render_template("login.html")
        
@app.route("/loginsuccess", methods = ['POST'])
def loginsuccess():
    if request.method == 'POST':
        email = request.form["email_name"]
        password = request.form["password"]
        user = Users(email, password, None, None)
        if user.fetch_user(email, password) is True:
            print("This is current user data", USERLIST)
            return render_template("dashboard.html")
        else:
            return render_template("login.html",text="The user does not exist.")

@app.route('/signup/')
def signup():
    return render_template("signup.html")

if __name__ == '__main__':
    app.run(debug=True)
