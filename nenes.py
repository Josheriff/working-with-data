class Nene(object):
    def __init__(self, nombre, edad, juguetes):
        self.nombre = nombre             # string
        self.edad = edad                 # int
        self.juguetes = juguetes         # lista / array, de diccionarios
        self.esta_registrado = False     # boolean
        self.karma = 0                   # int
    
    def mostrar_lista(self):
        if self.esta_registrado:
            self._listar_juguetes()
        else:
            print('EL NIÑO NO ESTA REGISTRADO EN EL SISTEMA')
    
    def _listar_juguetes(self):
        for indice, juguete in enumerate(self.juguetes):
            if juguete['mostrar'] and self.karma >= juguete['karma']:
                print(f'{indice} .- {juguete}')
    
   
