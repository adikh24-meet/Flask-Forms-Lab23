from flask import Flask, jsonify, request, render_template, redirect, url_for
import random

app = Flask(  # Create a flask app
	__name__,
	template_folder='templates',  # Name of html file folder
	static_folder='static'  # Name of directory for static files
)


username = "adikh"
password = "adi123"
facebook_friends=["ayoub","afu","juelle x2", "majd", "yasmin", "leen"]


@app.route('/', methods=['GET', 'POST'])  # '/' for the default page
def login():
  
    if request.method == 'POST':
        if request.form['username'] == username and request.form['password'] == password:
        	return redirect(url_for('home'))
        else:
        	return render_template('login.html')
    else:
        return render_template('login.html')

@app.route('/home')
def home():
    return render_template('home.html',friends=facebook_friends)

@app.route('/friend_exists/<string:name>')
def  friend_exists(name):
    		return render_template('friend_exists.html', name = name,friends=facebook_friends)

if __name__ == "__main__":  # Makes sure this is the main process
	app.run( # Starts the site
    debug=True
	)
