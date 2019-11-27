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
    else:
        db = sqlite3.connect('accounts.sqlite')
        query = db.execute(
            f'SELECT * FROM ACCOUNT WHERE username=\'{username}\' AND password=\'{password}\';')
        account = query.fetchall()
        if account:
            return render_template('survey.html')
            db.close()
        return render_template('index.html')
        db.close()


# def create_survey():
#   @app.route('/survey', methods=['POST'])

@app.route('/createaccount')
def create_page():
    return render_template('createaccount.html')


@app.route('/submitcreatepage', methods=["POST"])
def create_account():
    username = request.form.get('username')
    password = request.form.get('password')
    confirm_pass = request.form.get('confirmpass')
    if not username or not password or not confirm_pass:
        return "please fill out all forms"
    elif username and password and confirm_pass and password == confirm_pass:
        db = sqlite3.connect('accounts.sqlite')
        db.execute(
            f'INSERT INTO ACCOUNT VALUES (\'{username}\', \'{password}\') ')
        db.commit()
        return render_template('index.html')
        db.close()
    else:
        return 'please make sure that your confirmed password matches the one you put first!'
