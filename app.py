from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/createaccount.html')
def create_account():
    return render_template('createaccount.html')
