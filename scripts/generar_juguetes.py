from database import create_connection

primer_juguete = {'nombre': 'Oso Peluche',
 'precio':2, 'edad_recomendada': 1,
  'popularidad':0}

segundo_juguete = {'nombre': 'EscalesTrix',
 'precio':60, 'edad_recomendada': 9, 'popularidad':9}

tercer_juguete = {'nombre': 'Patines',
 'precio':60, 'edad_recomendada': 12,
  'popularidad':5}

juguetes = [primer_juguete, segundo_juguete, tercer_juguete] 

conn = create_connection()
def crear(data):
    nombre = data.get('nombre')
    precio = data.get('precio')
    edad_recomendada = data.get('edad_recomendada')
    popularidad = data.get('popularidad')

    with conn:
        sql = f''' INSERT INTO juguetes(nombre, precio, edad_recomendada, popularidad)
                VALUES("{nombre}", {precio}, {edad_recomendada}, {popularidad}) '''
        
        cur = conn.cursor()
        cur.execute(sql)
        print(cur.lastrowid)
        return cur.lastrowid

for juguete in juguetes:
    crear(juguete)