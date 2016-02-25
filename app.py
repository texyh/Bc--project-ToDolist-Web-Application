from flask import Flask, render_template, redirect, url_for, request, session, flash 
from todolist import ToDoList
from functools import wraps

app = Flask(__name__)
app.secret_key = "emeka"

def login_required(f):
	@wraps(f)
	def wrap(*args, **kwargs):
		if "logged_in" in session:
			return f(*args, **kwargs)
		else:
			flash('You need to login first')
			return redirect(url_for('signin'))
	return wrap


@app.route('/', methods = ['GET','POST'])
def signup():
	error = None
	if request.method  == 'POST':
		if request.form['email']!= 'admin':#or request.form['password']!= 'admin' :
			 error = 'Email is already found in our database'
		else:
			session["logged_in"] = True
			return redirect(url_for('inbox'))	
	return render_template('index.html', error=error )


@app.route('/welcome',methods = ['GET','POST'])
def signin():
	error = None
	#import pdb;pdb.set_trace()
	if request.method  == 'POST':

		if request.form['username']!= 'admin' or \
		request.form['password']!= 'admin' :
			 error = 'Invalid credentials. Please try again.'
		else:
			session["logged_in"] = True
			flash('you were just logged in!')
			return redirect(url_for('inbox'))
	return render_template('welcome.html')


@app.route('/inbox',methods = ['GET','POST'])
@login_required
def inbox():
	return render_template('inbox.html')


@app.route('/logout')
def logout():
	session.pop('logged_in',None)
	flash('you were just logged out!')
	return redirect(url_for('signup'))


if __name__ == "__main__":
	app.run(debug=True)