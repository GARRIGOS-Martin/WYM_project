from flask import Flask        
from flask import render_template, request


# Lance l'application
app = Flask(__name__) # instanciation application


@app.route("/")  # association d’une route (URL) avec la fonction suivante
def home():
    return render_template('/try_beau.html')   # on renvoie une chaîne de caractères

@app.route("/contact")  # association d’une route (URL) avec la fonction suivante
def contact():
    return render_template('/contact.html')   # on renvoie une chaîne de caractères

@app.route("/Thanks")  # association d’une route (URL) avec la fonction suivante
def thanks():
    return render_template('/Thanks.html')   # on renvoie une chaîne de caractères



app.run(debug = True, host='0.0.0.0', port=8888) # démarrage de l’appli

