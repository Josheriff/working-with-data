class Nene(object):
    def __init__(self, nombre, edad, adulto_a_cargo):
        self.nombre = nombre
        self.edad = edad
        self.adulto_a_cargo = adulto_a_cargo
    
    def __repr__(self):
        diccionario = {'nombre':self.nombre, 'edad':self.edad, "adulto_a_cargo":self.adulto_a_cargo.nombre}
        return f'{diccionario}'
