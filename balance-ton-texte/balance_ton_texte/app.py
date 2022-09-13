# Ceci est le projet de groupe de Sébastien, Noémie et Mohamed

from flask import Flask, render_template, url_for, request, flash, redirect
#from flask_sqlalchemy import SQLAlchemy


from forms import CommentaireForm  #c'est dans le fichier forms.py qui est dans le même dossier

app = Flask(__name__)

app.config['SECRET_KEY'] = '6cca083ea5392bae903fe796d5a6c5d7'
 #permet juste d'avoir une clé de sécurité, très utile contre les attaques de hacker classiques en ligne
# dans ce cas on importera sur python 'secrets' , et on génerera un token avec secrets.token_hex(16) et la réponse se met comme Secret_Key


list_comment = [] #liste de dictionnaires qui contiendra les commentaires : 5 éléments : 'nom' 'prenom' 'email' 'telephone' 'commentaire'
list_textes = [] #liste qui contiendra les textes que l'on demande à synthétiser


@app.route("/")
@app.route("/home")
def home():
	return render_template("home.html", title='Menu')

@app.route("/about")
def about():
	return render_template("about.html", title='about')

@app.route("/contact", methods=['GET', 'POST'])
def contact():
	form = CommentaireForm()   #form sera nos commentaires

	if form.validate_on_submit(): #si on vient de poster un commentaire valide
		flash(str(form.nom.data) + ', votre commentaire a bien été ajouté.', 'success')

		list_comment.append({'nom':form.nom.data, 'prenom':form.prenom.data, 'email':form.email.data,
		                      'telephone':form.telephone.data, 'commentaire':form.commentaire.data})

		return redirect(url_for('contacted'))
	return render_template("contact.html", title='contact', form=form)
	
	
@app.route("/contacted")
def contacted():
	return render_template("contacted.html", title='contacted')
		
@app.route("/model")
def model():
	return render_template("model.html", title='model')


if __name__ == '__main__':
	app.run(debug=True)
