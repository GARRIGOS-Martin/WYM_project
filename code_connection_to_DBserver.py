

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
    except:
        return False
  
conn = get_connection()
  
if conn:
    print("Connection to the PostgreSQL established successfully.")
else:
    print("Connection to the PostgreSQL encountered and error.")
conn.autocommit=True

# This program uses fetchall()

  
  
# CREATE A CURSOR USING THE CONNECTION OBJECT
curr = conn.cursor()
  
# EXECUTE THE SQL QUERY
curr.execute(" CREATE TABLE IF NOT EXISTS IDENTIFICATION (msg_id INT PRIMARY KEY NOT NULL, name VARCHAR(100), message VARCHAR(255) );")
curr.execute(" INSERT INTO IDENTIFICATION (msg_id, name,message) VALUES (1,'AMINA','Bonjour');")
#curr.execute("SELECT * FROM IDENTIFICATION ;")

# FETCH ALL THE ROWS FROM THE CURSOR
data = curr.fetchall()

  
# PRINT THE RECORDS
for row in data:
    print(row)
  
# CLOSE THE CONNECTION
conn.close()
