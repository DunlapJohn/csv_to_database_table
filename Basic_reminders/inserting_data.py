import psycopg2

DB_NAME = "rqrzygbx"
DB_USER = "rqrzygbx"
DB_HOST = "drona.db.elephantsql.com"
DB_PASS = "OWoytm0Ywk3hiFoFLSPNXOXC1H2npL5N"
DB_PORT = "5432"


conn = psycopg2.connect(database = DB_NAME, user = DB_USER, password = DB_PASS, host = DB_HOST, port = DB_PORT )

print('database connected successfully')

cur = conn.cursor() 

cur.execute("""
          CREATE TABLE CARBON
          (
          ID INT PRIMARY KEY NOT NULL,
          SYMBOL TEXT NOT NULL, 
          PRICE INT NOT NULL
          
          ) 
            """)
conn.commit()

print('table created successfully')