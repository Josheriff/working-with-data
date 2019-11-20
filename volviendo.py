from papas import Papa
from nenes import Nene
from database import create_connection

conn = create_connection()

nombre_padre = 'jose'
input_password = 'asereje'

consulta_sql = '''
               SELECT * FROM papas WHERE nombre="{nombre_padre}"
               '''
with conn:
    cur = conn.cursor()
    padre = cur.execute(consulta_sql).fetch()
    # padre = [1, 'jose', 'asereje']
    padre_id, nombre, password = padre
    papa = Papa(nombre, password, conn, padre_id)
    papa.check_password(input_password) # True/False

    print(padre)