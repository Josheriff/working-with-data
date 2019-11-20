import sqlite3
from sqlite3 import Error
from tablas import TABLA_JUGUETES, TABLA_NENES, TABLA_DESEOS_NENE,TABLA_PAPAS
 
def create_connection(db_file):
    """ create a database connection to a SQLite database """
    conn = None
    try:
        conn = sqlite3.connect(db_file)
    except Error as e:
        print(e)
 
    return conn

def create_tables(conn):
    cur = conn.cursor()
    cur.execute(TABLA_JUGUETES)
    cur.execute(TABLA_NENES)
    cur.execute(TABLA_DESEOS_NENE)
    cur.execute(TABLA_PAPAS)
 
 
if __name__ == '__main__':
    conn = create_connection("./persistence/persistence.db")
    create_tables(conn)