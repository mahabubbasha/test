#!/usr/local/bin/python

import psycopg2

def connect():
    """ Connect to the PostgreSQL database server """
    conn = None
    host=''
    database='edb'
    user='enterprisedb'
    password=''
    port='5444'
    
    drawing = open('./foo', 'rb').readlines()
    print (drawing)
    d= """adhadhjgadjgadjhadjhagd,
          bllaaallalal,,,, '''''
          """"""""
         helloooo
        """
    d = ''.join(drawing)
    print (d)
    exit(0)
    try:
        # read connection parameters
        conn = psycopg2.connect(host=host, dbname=database, user=user, password=password, port=port)
        cur = conn.cursor()
        #print('PostgreSQL database version:')
        #cur.execute('SELECT version()')
        #db_version = cur.fetchone()
        #print(db_version)
        cur.execute("INSERT INTO test_schema.PR(ID, SYNOPSIS, DESCRIPTION) " +
                    "VALUES(%s,%s,%s)",
                    (3, 'Test Synopsis for clob data', d))
        conn.commit()
        cur.close()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()
            print('Database connection closed.')

if __name__ == '__main__':
    connect()
