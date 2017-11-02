from flask import Flask, render_template, request, session

from .users import Users, USERLIST

from app import app

app.secret_key = "K!funguo51R1"

USERLIST.clear()

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
        user = Users("email@email.com", "password", "username", "name")
        if user.fetch_user(email, password) is True:
            print("This is the signup userlist",USERLIST)
            return render_template("signup.html", text="That user already exists.")
        else:
            print("This is the full userlist",USERLIST)
            user1 = Users(email, password, username, name)
            user1.add_user(email,password,username,name)
            return render_template("login.html")
        
@app.route("/loginsuccess", methods = ['POST'])
def loginsuccess():
    if request.method == 'POST':
        email = request.form["email_name"]
        password = request.form["password"]
        user2 = Users(email, password, None, None)
        if user2.fetch_user(email, password) is True:
            print(user2)
            session['logged_in'] = True
            return render_template("dashboard.html")
        else:
            return render_template("login.html",text="Wrong username/ password or the user does not exist.")

@app.route("/addRecipe", methods = ['POST'])
def addRecipe():
    category = request.form["category"]
    title = request.form["recipe_title"]
    lastUser = {}
    lastUser = USERLIST[-1]
    user3 = Users(lastUser["email"], lastUser["password"], lastUser["username"], lastUser["name"])
    user3.add_recipe(title, category)
    print(user3.category)   
    print(lastUser)
    return render_template("index.html")

@app.route('/signup/')
def signup():
    return render_template("signup.html")

@app.route('/logout/')
def logout():
    session.pop('logged_in',None)
    return render_template('login.html')
