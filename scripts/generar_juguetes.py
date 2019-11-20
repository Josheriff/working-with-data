from database import create_connection

TABLA_JUGUETES = """CREATE TABLE juguetes (
    juguete_id          INTEGER PRIMARY KEY,
    nombre              varchar NOT NULL,
    precio              INTEGER NOT NULL,
    edad_recomendada    INTEGER NOT NULL,
    popularidad         INTEGER NOT NULL
    );"""

primer_juguete = {'nombre': 'Oso Peluche',
 'precio':2, 'edad_recomendada': 1,
  'popularidad':0, 'mostrar': True}

segundo_juguete = {'nombre': 'EscalesTrix',
 'precio':60, 'edad_recomendada': 9, 'popularidad':9,
  'mostrar': True}

tercer_juguete = {'nombre': 'Patines',
 'precio':60, 'edad_recomendada': 12,
  'popularidad':5, 'mostrar': True} 

conn = create_connection()

def crear(conn):
    with conn:
        sql = f''' INSERT INTO nenes(nombre, precio, edad_recomendad, popularidad)
                VALUES("{nombre}", {edad}, {esta_registrado}, {karma}) '''
        
        cur = conn.cursor()
        cur.execute(sql)
        nene_id = cur.lastrowid
        return nene_id