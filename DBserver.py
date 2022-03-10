#To create a connection to the database server:
 
# poetry add psycopg2-binary
# ou
# pip install psycopg2

# librairy
import psycopg2
import os

# variable globale
max_id=0

# Connextion avec la BD
def get_connection():
    host = os.getenv('DB_HOST') # Va recuperer les variales d'environnement du container du docker compose
    user = os.getenv('DB_USER')
    password = os.getenv('DB_PASSWORD')
    port = os.getenv('DB_PORT')
    db = os.getenv('DB_NAME')
    try:
        conn = psycopg2.connect(
            database=db,
            user=user,
            password=password,
            host=host,
            port=port,
        )
        conn.autocommit=True
        return conn
    except:
        return False

def test_connection(connecteur):
    if connecteur:
        print("Connection to the PostgreSQL established successfully.")
    else:
        print("Connection to the PostgreSQL encountered and error.")

def create_table(curseur):
    curseur.execute(""" CREATE TABLE IF NOT EXISTS IDENTIFICATION (id INT PRIMARY KEY NOT NULL, 
                prenom VARCHAR(100), 
                nom VARCHAR(100), 
                mail VARCHAR(255),
                message VARCHAR(255));""")
    global max_id 
    curseur.execute ('SELECT MAX (id) FROM IDENTIFICATION ;')
    data = curseur.fetchall()
    print(len(data))
    # Recherche l'id max 
    max_id = ((data[0][0])or 0)+1  # 0 si data[0][0] est None (quand la table est vide))
    print ("table créée")

def insert_data(curseur, var1, var2, var3, var4 ):
    global max_id 
    print(f" INSERT INTO IDENTIFICATION (id, prenom, nom, mail, message) VALUES ({max_id}, {var1},{var2},{var3}, {var4});")
    curseur.execute(f" INSERT INTO IDENTIFICATION (id, prenom, nom, mail, message) VALUES ({max_id}, {var1},{var2},{var3}, {var4});")
    max_id+=1
    print("data ajouté")

def close_connection(connection):
    connection.close() 

