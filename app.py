from flask import Flask        
from flask import render_template, request
from DBserver import *
import requests

# Connexion à la Base de donnée et création de la table
conn = get_connection()
print (conn)
curr = conn.cursor()
test_connection(conn)   # Teste la connection
create_table(curr)      # Creation de la table

# Recupere l'id max



# Lance l'application
app = Flask(__name__) # instanciation application

@app.route("/")  # association d’une route (URL) avec la fonction suivante
def home():
    return render_template('/home.html')   # on renvoie une chaîne de caractères

@app.route("/home")  # association d’une route (URL) avec la fonction suivante
def return_home():
    return render_template('/home.html')   # on renvoie une chaîne de caractères

@app.route("/contact")  # association d’une route (URL) avec la fonction suivante
def contact():
    return render_template('/contact.html')   # on renvoie une chaîne de caractères

@app.route("/about")  # association d’une route (URL) avec la fonction suivante
def about():
    return render_template('/about.html')   # on renvoie une chaîne de caractères

@app.route("/Thanks", methods=["GET", "POST"])  # association d’une route (URL) avec la fonction suivante
def thanks():
    prenom = "'" + request.form.get("Prenom") + "'"
    nom = "'" + request.form.get("Nom") + "'"
    mail = "'" + request.form.get("Mail") + "'"
    message = "'" + request.form.get("Message") + "'"
    
    print(prenom, nom, message, mail)
    insert_data(curr, prenom, nom, mail, message)

    return render_template('Thanks.html') 

@app.route("/summary" , methods=["GET","POST"])  # association d’une route (URL) avec la fonction suivante
def summary():
    text = request.form.get("input_text")
    texte_resume = resume_texte_ibm(text)    
    return render_template('summary.html',
                            texte_initial= text,
                            texte_resume = texte_resume)   # on renvoie une chaîne de caractères


def resume_texte_ibm(monText):
    # Pour interagir avec la page html  
    url = "http://localhost:5000/model/predict"

    headers= {"Content-Type": "application/json; charset=utf-8", "accept":"application/json"}
    data  = { "text": [monText]}

    r = requests.post(url, json=data)

    return r.text


app.run(debug = True, host='0.0.0.0', port=8888) # démarrage de l’appli

# Deconnection de la Base de donnée
close_connection()


