from numpy import row_stack
import psycopg2

DB_NAME = "rqrzygbx"
DB_USER = "rqrzygbx"
DB_HOST = "drona.db.elephantsql.com"
DB_PASS = "OWoytm0Ywk3hiFoFLSPNXOXC1H2npL5N"
DB_PORT = "5432"


conn = psycopg2.connect(database = DB_NAME, user = DB_USER, password = DB_PASS, host = DB_HOST, port = DB_PORT )

print('database connected successfully')

cur = conn.cursor() 

cur.execute("SELECT ID, SYMBOL, PRICE FROM carbon")

row = cur.fetchall()
for data in row:
    print("ID : " + str(data[0]))
    print("SYMBOL :" + data[1])
    print("PRICE : "  + str(data[2]))
      
print('data selected successfully')
conn.close() 