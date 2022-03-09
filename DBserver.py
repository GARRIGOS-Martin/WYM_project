#sudo docker run --name wym_db -e POSTGRES_PASSWORD=admin -e POSTGRES_USER=wym_admin -p 5432:5432 -d postgres 
#poetry install psycopg2
#poetry add psycopg2-binary
#pip install psycopg2


#the following code can be used to create a connection to the database server:
import psycopg2


def get_connection():
    try:
        conn = psycopg2.connect(
            database="postgres",
            user="wym_admin",
            password="admin",
            host="127.0.0.1",
            port=5432,
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
    print ("table créée")

def insert_data(curseur, id, var1, var2, var3, var4 ):
    print(f" INSERT INTO IDENTIFICATION (id, prenom, nom, mail, message) VALUES ({id}, {var1},{var2},{var3}, {var4});")
    curseur.execute(f" INSERT INTO IDENTIFICATION (id, prenom, nom, mail, message) VALUES ({id}, {var1},{var2},{var3}, {var4});")
    """
    data = curseur.fetchall()
    for row in data:
        print(row)
    """
    print("data ajouté")

def close_connection(connection):
    connection.close() 

