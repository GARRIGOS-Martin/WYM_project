from flask import Flask        # import de l’objet Flask
from flask import render_template 

app = Flask(__name__) # instanciation application

@app.route("/")  # association d’une route (URL) avec la fonction suivante
def home():
    return render_template('/home.html')   # on renvoie une chaîne de caractères

@app.route("/contact")  # association d’une route (URL) avec la fonction suivante
def contact():
    return render_template('/contact.html')   # on renvoie une chaîne de caractères

<<<<<<< HEAD
@app.route("/Thanks")  # association d’une route (URL) avec la fonction suivante
def thanks():
    return render_template('Thanks.html')   # on renvoie une chaîne de caractères
app.run(debug = True) # démarrage de l’appli
=======
@app.route("/nom")
def nom(text='pas de résumé'):
    sentiment = "négatif"
    if sentiment == "positif":
        text="ce résumé est positif"
    else :
        text= "ce résumé est négatif"
    return render_template('/nom.html',text=text) 

app.run(debug=True) # démarrage de l’appli
 
 
>>>>>>> 76a4bd1fc8238b469fa7869f2f32b250be2fec02
