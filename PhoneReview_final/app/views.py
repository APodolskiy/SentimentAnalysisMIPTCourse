from flask import render_template, request
from codecs import open
import time
from sentiment_classifier import SentimentClassifier
from app import app

print "Preparing classifier"
start_time = time.time()
classifier = SentimentClassifier()
print "Classifier is ready"
print time.time() - start_time, "seconds"

@app.route('/')
@app.route('/index')
def index():
    user = {'nickname': 'Miguel'}
    return render_template("index.html", title='Home', user=user)

@app.route('/mra', methods = ['GET', 'POST'])
def mra(text="", prediction_message=""):
    if request.method == 'POST':
        if request.form['submit'] == 'estimate':
            text = request.form["text"]
            logfile = open("mra_logs.txt", "a", "utf-8")
            print >> logfile, "<response>"
            print >> logfile, text
            prediction_message = classifier.get_prediction_message(text)
            print prediction_message
            print >> logfile, prediction_message
            print >> logfile, "</response>"
            logfile.close()
        if request.form['submit'] == 'clear':
            text = ""
            prediction_message = ""
    return render_template('review_analysis.html',
                           title='PR Analyzer', text=text, prediction_message=prediction_message)