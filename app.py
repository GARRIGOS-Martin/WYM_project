from flask import Flask        # import de l’objet Flask
from flask import render_template 

app = Flask(__name__) # instanciation application

@app.route("/")  # association d’une route (URL) avec la fonction suivante
def home():
    return render_template('/home.html')   # on renvoie une chaîne de caractères

@app.route("/contact")  # association d’une route (URL) avec la fonction suivante
def contact():
    
    return render_template('contact.html')   # on renvoie une chaîne de caractères

app.run(debug=True) # démarrage de l’appli