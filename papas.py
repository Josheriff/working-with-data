from nenes import Nene

class Papa(object):
    def __init__(self, nombre):
        self.nombre = nombre
        self.nenes_a_cargo = []
    
    def registrar_nene(self, nombre, edad):
        adulto_a_cargo = self
        nene = Nene(nombre, edad, adulto_a_cargo)
        self.nenes_a_cargo.append(nene)