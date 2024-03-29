class Nene(object):
    def __init__(self, nene_data, conn, nene_id=0):
        self.nene_id = nene_id
        self.nombre = nene_data.get('nombre')             # string
        self.edad = nene_data.get('edad')                 # int
        self.juguetes = nene_data.get('juguetes')         # lista / array, de diccionarios
        self.esta_registrado = False     # boolean
        self.karma = 0                   # int
        self.conn = conn
    
    def mostrar_lista(self):
        if self.esta_registrado:
            self._listar_juguetes()
        else:
            print('EL NIÑO NO ESTA REGISTRADO EN EL SISTEMA')
    
    def _listar_juguetes(self):
        juguetes_en_venta = list()
        sql = f''' SELECT * FROM juguetes
                   WHERE edad_recomendada <= {self.edad}
                   AND popularidad <= {self.karma}
                   ;'''
        with self.conn:
            cur = self.conn.cursor()
            juguetes_en_venta = cur.execute(sql).fetchall()
            print(juguetes_en_venta)

        for indice, juguete in enumerate(juguetes_en_venta):
            print(f'{indice} .- {juguete[1]}')
    
    def crear(self):
        with self.conn:
            esta_registrado = 1 if self.esta_registrado else 0
            sql = f''' INSERT INTO nenes(nombre, edad, esta_registrado, karma)
                    VALUES("{self.nombre}", {self.edad}, {esta_registrado}, {self.karma}) '''
            
            cur = self.conn.cursor()
            cur.execute(sql)
            self.nene_id = cur.lastrowid
            return self.nene_id
    
    def save(self):
        with self.conn:
            esta_registrado = 1 if self.esta_registrado else 0
            sql = f''' UPDATE nenes 
                    SET nombre = "{self.nombre}", edad={self.edad}, esta_registrado={esta_registrado}, karma={self.karma}
                    WHERE nene_id={self.nene_id} ;'''
            
            cur = self.conn.cursor()
            cur.execute(sql)
            return
            
    
   
