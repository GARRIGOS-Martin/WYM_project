from flask import Flask        # import de l’objet Flask
from flask import render_template 

app = Flask(__name__) # instanciation application

@app.route("/")  # association d’une route (URL) avec la fonction suivante
def home():
    return render_template('/home.html')   # on renvoie une chaîne de caractères

@app.route("/contact")  # association d’une route (URL) avec la fonction suivante
def contact():
    return render_template('/contact.html')   # on renvoie une chaîne de caractères

@app.route("/nom")
def nom(text='pas de résumé'):
    sentiment = "négatif"
    if sentiment == "positif":
        text="ce résumé est positif"
    else :
        text= "ce résumé est négatif"
    return render_template('/nom.html',text=text) 

app.run(debug=True) # démarrage de l’appli
 
 