import functions_automation as c
import pandas as pd
import psycopg2

# fill in variables - the script then takes all the csv within the \
    # directory and uploads them to tables corresponding to the names of the csv files. 
    
# variables 
DB_NAME = "AAAA"
DB_USER = "AAAA"
DB_HOST = "ABC.com"
DB_PASS = "XXXX"
DB_PORT = "5432" # Probably 

host = DB_HOST
dbname = DB_NAME
user = DB_USER
password = DB_PASS
dataset_dir = 'datasets'
csv_files = c.csv_files()

c.configure_dataset_directory(csv_files, dataset_dir)
df = c.create_df(dataset_dir, csv_files)

for k in csv_files:

    #call dataframe
    dataframe = df[k]

    #clean table name
    tbl_name = c.clean_tbl_name(k)
    
    #clean column names
    col_str, dataframe.columns = c.clean_colname(dataframe)
    
    #upload data to db   
    c.upload_to_db(DB_HOST, 
                 DB_NAME, 
                 DB_USER, 
                 DB_PASS, 
                 tbl_name, 
                 col_str, 
                 file=k, 
                 dataframe=dataframe, 
                 dataframe_columns=dataframe.columns)
    conn = psycopg2.connect(database = DB_NAME, user = DB_USER, password = DB_PASS, host = DB_HOST, port = DB_PORT)


    cur = conn.cursor()
    print('opened database successfully')
    # dropping any tables 
    cur.execute("drop table if exists %s;" % (tbl_name))
    print('dropped database successfully')
    # create table(s)
    cur.execute("CREATE TABLE %s (%s )" % (tbl_name, col_str))
    print('{0}created successfully'.format(tbl_name))
    #turn df back into a csv
    dataframe.to_csv(k, header=dataframe.columns, index=False, encoding='utf-8' )
    #open that csv in memory
    my_file = open(k)
    print('file opened in mem')
    #copy the opened csv(s) to the database
    SQL_statement = """
    COPY %s from STDIN WITH
    CSV
    HEADER
    DELIMITER AS ','
    """
    cur.copy_expert(sql=SQL_statement % tbl_name, file=my_file )
    print(' file copied to db')
    # public
    cur.execute("grant select on table %s to public" % tbl_name)
    conn.commit()
    conn.close()
    print('table {0} imported to %s' % tbl_name)
print('all tables have been successfully imported to the database')