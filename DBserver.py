#sudo docker run --name wym_db -e POSTGRES_PASSWORD=admin -e POSTGRES_USER=wym_admin -p 5432:5432 -d postgres 
#poetry install psycopg2
#poetry add psycopg2-binary
#pip install psycopg2


#the following code can be used to create a connection to the database server:
import psycopg2


def get_connection():
    try:
        return psycopg2.connect(
            database="postgres",
            user="wym_admin",
            password="admin",
            host="127.0.0.1",
            port=5432,
        )
        conn.autocommit=True
    except:
        return False

def test_connection():
    conn = get_connection()
  
    if conn:
        print("Connection to the PostgreSQL established successfully.")
    else:
        print("Connection to the PostgreSQL encountered and error.")

def create_table():
    curr.execute(" CREATE TABLE IF NOT EXISTS IDENTIFICATION (msg_id INT PRIMARY KEY NOT NULL, name VARCHAR(100), message VARCHAR(255), objet VARCHAR(255));")
    print ("table crée")

def insert_data():
    
    curr.execute(" INSERT INTO IDENTIFICATION (msg_id, name,message,objet) VALUES (1,'AMINA','Bonjour', 'fff');")
    data = curr.fetchall()
    for row in data:
        print(row)
    
    print("data ajouté")

def close_connection():
    conn.close() 

