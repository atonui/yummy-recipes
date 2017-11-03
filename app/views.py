from flask import Flask, render_template, request, session

from .users import Users, USERLIST

from .categories import Categories

from app import app

app.secret_key = "K!funguo51R1"

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/login/')
def login():
    return render_template("login.html")

@app.route("/signupsuccess", methods=['POST'])
def signupsuccess():
    email = request.form["email_name"]
    password = request.form["password"]
    username = request.form["username"]
    name = request.form["name"]
    print(USERLIST)
    try:
        if USERLIST:
            for item in USERLIST:
                if email == item.email and password == item.password:
                    print("This is the signup userlist", USERLIST)
                    return render_template("signup.html", text="That user already exists.")           
        else:
            user = Users(email, password, username, name)
            USERLIST.append(user)
            print("This is the full userlist", USERLIST)
            return render_template("login.html")
    except:
        return render_template("error.html")
        
@app.route("/loginsuccess", methods = ['POST'])
def loginsuccess():
    if request.method == 'POST':
        email = request.form["email_name"]
        password = request.form["password"]
        #user2 = Users(email, password, None, None)
        if USERLIST:
            for item in USERLIST:
                if email in item.email and password in item.password:
                    session['logged_in'] = True
                    return render_template("dashboard.html")
        else:
            return render_template("login.html",text="Wrong username/ password or the user does not exist.")

@app.route("/addCategory", methods = ['POST'])
def addCategory():
    description = request.form["category"]
    title = request.form["recipe_title"]
    try:
        currentUser = USERLIST[-1]
    
    # user3 = Users(lastUser["email"], lastUser["password"], lastUser["username"], lastUser["name"])
    # user3.add_recipe(title, category)
    # print(user3.category)   
    # print(lastUser)
        new_category = Categories(title, description)
        currentUser.category.append(new_category)
        return render_template("categories.html", value = title, value2 = description)
    except:

        return render_template("error.html")

@app.route('/signup/')
def signup():
    return render_template("signup.html")

@app.route('/logout/')
def logout():
    session.pop('logged_in',None)
    return render_template('login.html')
