from flask import Flask, render_template, request
import sqlite3

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/loggedin', methods=['POST'])
def verify_login():
    username = request.form.get('username')
    password = request.form.get('password')
    if not username or not password:
        return render_template('failpage.html')
    return render_template('survey.html')
    #     try:
    #         db = sqlite3.connect('accounts.sqlite')
    #     except:
    #         print('database error')
    #     query = db.execute('SELECT * FROM ACCOUNT;')
    #     if username in query and password in query:
    #         return render_template('survey.html')
    # else:


'''
@app.route('/survey', methods=['POST'])
def create_survey():
'''

'''
@app.route('/createaccount.html')
def create_page():
    return render_template('createaccount.html')
'''
