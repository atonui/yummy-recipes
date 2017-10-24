from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def index():
    return render_template("/index.html")

@app.route('/login/')
def login():
    if request.method =='POST':
        email=request.form["email_name"]
        password = request.form["password_name"]
        return render_template("/index.html")

if __name__=='__main__':
    app.run(debug=True)