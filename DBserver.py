#sudo docker run --name wym_db -e POSTGRES_PASSWORD=admin -e POSTGRES_USER=wym_admin -p 5432:5432 -d postgres 
#poetry install psycopg2
#poetry add psycopg2-binary
#pip install psycopg2


#the following code can be used to create a connection to the database server:
import psycopg2
import os

mid=0
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
    global mid 
    curseur.execute ('SELECT MAX (id) FROM IDENTIFICATION ;')
    data = curseur.fetchall()
    print(len(data))
    mid = ((data[0][0])or 0)+1
    print ("table créée")

def insert_data(curseur, var1, var2, var3, var4 ):
    global mid 
    print(f" INSERT INTO IDENTIFICATION (id, prenom, nom, mail, message) VALUES ({mid}, {var1},{var2},{var3}, {var4});")
    curseur.execute(f" INSERT INTO IDENTIFICATION (id, prenom, nom, mail, message) VALUES ({mid}, {var1},{var2},{var3}, {var4});")
   
    # data = curseur.fetchall()
    # for i in data:
    #     rowid =i.id
    #     rowid=max(rowid)
    #     print(rowid)
    
    mid+=1
    print("data ajouté")

def close_connection(connection):
    connection.close() 

