from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
@app.route('/home')
def home():
	return render_template('home.html')
@app.route('/assignments')
def about():
	return render_template('assignments.html')
if __name__ == "__main__":
	app.run(debug=True)