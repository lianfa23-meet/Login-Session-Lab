from flask import Flask, render_template, request, url_for, redirect
from flask import session as login_session


app = Flask(__name__)
app.config['SECRET_KEY'] = 'super-secret-key'


@app.route('/', methods=['GET', 'POST'])
def home():
	if request.method == 'POST':
		try:
			author = request.form['Author']
			age = request.form['Age']
			quote = request.form['Quote']
			post=[author, age, quote]
			print("step1")
			try:
				posts = login_session['posts']
				posts.append(post)
				login_session['posts'] = posts
				print("step2")
			except:
				login_session['posts'] = [post]
				print("step3")
			return render_template('thanks.html')

		except:
			return render_template('error.html')


	else:

		return render_template('home.html')

@app.route('/error')
def error():

	return render_template('error.html')


@app.route('/display')
def display():

	return render_template('display.html', posts=login_session['posts'])


@app.route('/thanks')
def thanks():

	return render_template('thanks.html')


if __name__ == '__main__':
	app.run(debug=True)