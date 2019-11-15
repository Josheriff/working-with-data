class Nene(object):
    def __init__(self, nombre, edad, juguetes):
        self.nombre = nombre
        self.edad = edad
        self.juguetes = juguetes
        self.esta_registrado = False
    
    def mostrar_lista(self):
        if self.esta_registrado:
            self._listar_juguetes()
        else:
            print('EL NIÑO NO ESTA REGISTRADO EN EL SISTEMA')
    
    def _listar_juguetes(self):
        for indice, juguete in enumerate(self.juguetes):
            if juguete['mostrar']:
                print(f'{indice} .- {juguete}')
    
   
