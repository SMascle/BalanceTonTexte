# Ceci est le projet de groupe de Sébastien, Noémie et Mohamed

from flask import Flask, render_template, url_for, request

app = Flask(__name__)


liste_noms = []


@app.route("/")
@app.route("/home")
def home():
	return render_template("home.html", title='Menu')

@app.route("/about")
def about():
	return render_template("about.html", title='about')

@app.route("/contact")
def contact():
	return render_template("contact.html", title='contact')
	
	
@app.route("/contacted")
def contacted():
	return render_template("contacted.html", title='contacted')
		
@app.route("/model")
def model():
	return render_template("model.html", title='model')


if __name__ == '__main__':
	app.run(debug=True)
