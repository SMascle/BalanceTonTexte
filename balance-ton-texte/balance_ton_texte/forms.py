from flask_wtf import FlaskForm
from wtforms import StringField #permet de faire facilement ces classes qui servent pour faire un registre sur un site
from wtforms import SubmitField #permet de faire un submit pour valider toutes les données qu'on entre

from wtforms.validators import DataRequired #permet de faire des validations
from wtforms.validators import Length #valide si on a un nombre choisi de caractères
from wtforms.validators import Email #permet de voir si on a une bonne nomenclature d'emmail





class CommentaireForm(FlaskForm):
    nom = StringField('Nom', validators=[DataRequired(),
                                                   Length(min=2, max=250, message='Nom non valide')])  #permet de dire qu'un nom fait au moins 2 lettres et max 250
    # validators servent à valider que c'est valide
    prenom = StringField('Prenom', validators=[DataRequired(),
                                                   Length(min=2, max=250, message='Prénom non valide')])  #permet de dire qu'un prénom fait au moins 2 lettres et max 250
    # validators servent à valider que c'est valide

    email = StringField('Email', validators=[DataRequired(),
                                                   Email(message = 'mail non valide')])  #permet de faire un email
  
    telephone = StringField('Telephone', validators=[
                                                   Length(max=16)])  #numero entre 0 et 16, il faut aussi apprendre à le laisser optionelle ?

    commentaire = StringField('Commentaire', validators=[DataRequired(),
                                                   Length(min=2, max=500)])  #commentaire entre 2 et 500 lettres

    submit = SubmitField('Postez')                                               

