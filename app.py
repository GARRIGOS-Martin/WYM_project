from flask import Flask, render_template # import de l’objet Flask

app = Flask(__name__) # instanciation application

@app.route("/")  # association d’une route (URL) avec la fonction suivante
def home():
    return render_template('page1.html')   # on renvoie une chaîne de caractères

@app.route("/contact")  # association d’une route (URL) avec la fonction suivante
def contact():
    return render_template('contact.html')   # on renvoie une chaîne de caractères

<<<<<<< HEAD
app.run(debug = True) # démarrage de l’appli
=======
app.run() # démarrage de l’appli
>>>>>>> b9523b3381b3957e6b579f771204d680dc5097c5
