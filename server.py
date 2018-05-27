from flask import Flask, render_template, redirect, request, session
import random
app = Flask(__name__)
app.secret_key = "Keepthisasecret"

@app.route('/')
def index():
  session['number'] = random.randint(0, 100)
  return render_template('index.html')

@app.route('/guess', methods=['POST'])
def result():
  if int(request.form['guess']) == session['number']:
    answer = "Correct"
    return render_template("index.html", answer=answer)
  elif int(request.form['guess']) < session['number']:
    answer = "Too Low"
    return render_template('index.html', answer=answer)
  elif int(request.form['guess']) > session['number']:
    answer = "Too High"
    return render_template('index.html', answer=answer)
app.run(debug=True)