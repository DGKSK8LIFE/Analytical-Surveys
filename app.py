from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/loggedin', methods=["POST"])
def verify_login():
    username = request.form.get("username")
    password = request.form.get("password")
    return username, password


@app.route('/createaccount.html')
def create_page():
    return render_template('createaccount.html')
