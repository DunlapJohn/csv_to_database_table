import psycopg2

DB_NAME = "rqrzygbx"
DB_USER = "rqrzygbx"
DB_HOST = "drona.db.elephantsql.com"
DB_PASS = "OWoytm0Ywk3hiFoFLSPNXOXC1H2npL5N"
DB_PORT = "5432"

try: 
    conn = psycopg2.connect(database = DB_NAME, user = DB_USER, password = DB_PASS, host = DB_HOST, port = DB_PORT )
    print('databse connected successfully')
except: 
    print("database not connected")