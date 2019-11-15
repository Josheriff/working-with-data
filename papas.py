from nenes import Nene

class Papa(object):
    def __init__(self, nombre):
        self.nombre = nombre
        self.nenes_a_cargo = []
    
    def registrar_nene(self, nene):
        self.nenes_a_cargo.append(nene)
        nene.esta_registrado = True
    
    def restringir_lista_por_edad(self, nene, edad):
        if nene in self.nenes_a_cargo:
            for juguete in nene.juguetes:
                if juguete['edad_recomendada'] > edad:
                    juguete['mostrar'] = False
    
