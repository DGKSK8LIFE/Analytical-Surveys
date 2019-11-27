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
    db_account = request.form.get(f'{username}|{password}')
    if not username or not password:
        return render_template('failpage.html')
    else:
        db = sqlite3.connect('accounts.sqlite')
        query = db.execute(
            f'SELECT * FROM ACCOUNT WHERE username=\'{username}\';')
        if dbaccount in query:
            return render_template('survey.html')
        else:
            return render_template('index.html')


'''
@app.route('/survey', methods=['POST'])
def create_survey():
'''

'''
@app.route('/createaccount.html')
def create_page():
    return render_template('createaccount.html')
'''
