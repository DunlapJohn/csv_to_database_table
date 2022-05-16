import psycopg2

DB_NAME = "AAAA"
DB_USER = "AAAA"
DB_HOST = "ABC.com"
DB_PASS = "XXXX"
DB_PORT = "5432" # Probably 


conn = psycopg2.connect(database = DB_NAME, user = DB_USER, password = DB_PASS, host = DB_HOST, port = DB_PORT )

print('database connected successfully')

cur = conn.cursor() 

cur.execute("UPDATE carbon SET SYMBOL = 'CA-CBC' WHERE ID = 1")

conn.commit()
print('data updated successfully')
print("total row effected" + str(cur.rowcount))

