from flask import Flask, render_template, request
import sqlite3
import os

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
            db.close()
            return render_template('survey.html')
        db.close()
        return render_template('index.html')
        # db.close()


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
        os.mkdir(f'/home/tarekali/AnalyticSurveys/user_surveys/{username}')
        db = sqlite3.connect('accounts.sqlite')
        db.execute(
            f'INSERT INTO ACCOUNT VALUES (\'{username}\', \'{password}\') ')
        db.commit()
        db.close()
        return render_template('index.html')

    else:
        return 'please make sure that your confirmed password matches the one you put first!'


@app.route('/survey', methods=['POST'])
def parse_input_and_insert_it():
    title = request.form.get('title')
    question_one = request.form.get('question_one')
    question_two = request.form.get('question_two')
    question_three = request.form.get('question_three')
    question_four = request.form.get('question_four')
    question_five = request.form.get('question_five')
    question_six = request.form.get('question_six')
    if title and question_one and question_two and question_three and question_four and question_five and question_six:
        template_to_write = render_template('surveytemplate.html', title=title, question_one=question_one, question_two=question_two,
                                                   question_three=question_three, question_four=question_four, question_five=question_five, question_six=question_six)
    else:
        return "please fill out all forms"
