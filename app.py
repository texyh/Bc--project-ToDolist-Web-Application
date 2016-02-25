from flask import Flask, render_template, redirect, url_for, request 
from todolist import ToDoList

app = Flask(__name__)

@app.route('/', methods = ['GET','POST'])
def Home():
	error = None
	if request.method  == 'POST':
		
		if request.form['username']!= 'admin' or request.form['password']!= 'admin' :
			 error = 'Invalid credentials. Please try again.'
		else:
			return redirect(url_for('inbox'))

		#import pdb;pdb.set_trace()

		

	return render_template('index.html', error=error )


@app.route('/welcome')
def welcome():
	return render_template('welcome.html')


@app.route('/inbox',methods = ['GET','POST'])
def inbox():
	emeka = ToDoList()
	if request.method == 'POST':
		#import pdb;pdb.set_trace()
		new_todo = request.form['todo']
		emeka.create(new_todo)
	return emeka.list()
	return render_template('inbox.html')

if __name__ == "__main__":
	app.run(debug=True)