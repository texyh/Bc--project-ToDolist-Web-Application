from flask import Flask, render_template, redirect, \
url_for, request, session, flash, g 
from functools import wraps
import sqlite3
 ''' first i inititalized the flask object
     then i set the secret key for managing session
     the i created and instance of the database module
 '''


app = Flask(__name__)
app.secret_key = "emeka"
app.database = "todo.db"

#the loginrequired decorator
def login_required(f):
	@wraps(f)
	def wrap(*args, **kwargs):
		if "logged_in" in session:
			return f(*args, **kwargs)
		else:
			return redirect(url_for('signin'))
	return wrap

#the signup decorator
@app.route('/', methods = ['GET','POST'])
def signup():
    error = None
    if request.method  == 'POST':
        g.db = connect_db()
        cur = g.db.execute('select * from user')
        for i in cur:
            if i[2]==request.form['email']:
                error ="Email exist in our datebase"    
            else:
                g.db.execute('INSERT INTO user VALUES("request.form[firstname]",\
                    "request.form[lastname]","request.form[email]","request.form[password]")')
                session["logged_in"] = True
                return redirect(url_for('inbox'))
    return render_template('index.html', error=error )

#the signin decorator
@app.route('/welcome',methods = ['GET','POST'])
def signin():
    error = None
    if request.method  == 'POST':
        g.db = connect_db()
        cur = g.db.execute('select * from user')
        for i in cur:
            if i[2]==request.form['email'] and i[3] == request.form['password']:
                session["logged_in"] = True
                return redirect(url_for('inbox'))
            else:
                error = 'Invalid credentials. Please try again.'
    return render_template('welcome.html')

#the loginrequired decorator
@app.route('/inbox',methods = ['GET','POST'])
@login_required
def inbox():
	return render_template('inbox.html')

#the logout decorator
@app.route('/logout')
def logout():
	session.pop('logged_in',None)
	return redirect(url_for('signup'))


def connect_db():
    return sqlite3.connect(app.database)




if __name__ == "__main__":
	app.run(debug=True)