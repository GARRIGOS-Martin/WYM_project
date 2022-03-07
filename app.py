from flask import Flask # import de l’objet Flask

app = Flask(__name__) # instanciation application

@app.route("/")  # association d’une route (URL) avec la fonction suivante
def home():
    return "<p>Bienvenue chez moi</p>"   # on renvoie une chaîne de caractères

app.run() # démarrage de l’appli