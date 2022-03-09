from flask import Flask        # import de l’objet Flask
from flask import render_template, request
#import requests


app = Flask(__name__) # instanciation application

@app.route("/")  # association d’une route (URL) avec la fonction suivante
def home():
    return render_template('/home.html')   # on renvoie une chaîne de caractères

@app.route("/contact")  # association d’une route (URL) avec la fonction suivante
def contact():
    return render_template('/contact.html')   # on renvoie une chaîne de caractères

@app.route("/Thanks")  # association d’une route (URL) avec la fonction suivante
def thanks():
    return render_template('Thanks.html')   # on renvoie une chaîne de caractères

@app.route("/summary" , methods=["GET","POST"])  # association d’une route (URL) avec la fonction suivante
def summary():
    text = request.form.get("input_text")
    texte_resume = resume_texte_ibm(text)
    
def get_data():
   if request.method == 'POST':
      result = request.form
      return render_template("result.html",result = result)


def resume_texte_ibm(monText):

    # Pour interagir avec la page html  
    url = "http://localhost:5000/model/predict"

    headers= {"Content-Type": "application/json; charset=utf-8", "accept":"application/json"}
    data  = { "text": [monText]}

    r = requests.post(url, json=data)

    return r.text



app.run(debug = True, host='0.0.0.0', port=8888) # démarrage de l’appli


