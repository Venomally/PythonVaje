from flask import Flask, redirect, url_for, request, render_template
import random
app = Flask(__name__)

us_pass = {'martin' : 'martin00', 'student' : 'student00'}

@app.route('/success/<token>/<name>', methods = ['GET'])
def success(name,token):
    return f"<h1>Zdravo , {name}. Vas token je {token}</h1>"

@app.route('/failure', methods = ['GET'])
def failure():
    return 'Wrong username or password'

@app.route('/login', methods = ['POST', 'GET'])
def login():
    if request.method == 'GET':
        return render_template('login.html')
    if request.method == 'POST':
        user = request.form['username']
        password = request.form['password']
        
        try:
            if us_pass[user] == password:
                random_string = str(random.randion(1000,9999))
                return redirect(url_for('success',name = user))  
            else:
                return redirect(url_for('failure',name = user))
        except:
            return redirect(url_for('failure',name = user))


app.run(host='127.0.0.1',debug=True, port=1235, use_reloader=False)
