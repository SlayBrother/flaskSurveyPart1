from flask import Flask, request, render_template, redirect, flash, jsonify
from random import randint, choice, sample
from flask_debugtoolbar import DebugToolbarExtension
from surveys import satisfaction_survey

app = Flask(__name__)

app.config['SECRET_KEY'] = "colby_is_cool69420"
app.config['DEBUG_TB_INTERCEPT_REDIRECTS'] = False
debug = DebugToolbarExtension(app)

RESPONSES = []

@app.route('/')
def home_link():
    return render_template('home.html')

@app.route('/satis_questions')
def satisfaction_questions1():
    return render_template('satis_questions.html', survey=satisfaction_survey)

@app.route('/satis_questions2')
def satisfaction_questions2():
    return render_template('satis_questions2.html', survey=satisfaction_survey)

@app.route('/satis_questions3')
def satisfaction_questions3():
    return render_template('satis_questions3.html', survey=satisfaction_survey)

@app.route('/satis_questions4')
def satisfaction_questions4():
    return render_template('satis_questions4.html', survey=satisfaction_survey)

@app.route('/thanks')
def thanks_link():
    return render_template('thanks.html')

@app.route('/personality')
def pers_link():
    return render_template('personality.html')


@app.route('/submit_survey', methods=['POST'])
def submit_survey():
    responses = {}
    for question in satisfaction_survey.questions:
        question_text = question.question
        if question.choices:
            responses[question_text] = request.form.get(question_text)
    RESPONSES.append(responses)
    flash('Thank you for submitting the survey!')
    return redirect('/')