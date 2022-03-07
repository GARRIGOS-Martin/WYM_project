from flask import Flask, render_template # import de l’objet Flask



app = Flask(__name__) # instanciation application

@app.route("/")  # association d’une route (URL) avec la fonction suivante
def home():
    return render_template('/page1.html')   # on renvoie une chaîne de caractères

app.run() # démarrage de l’appli