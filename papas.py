from nenes import Nene

class Papa(object):
    def __init__(self, nombre, conn):
        self.nombre = nombre
        self.nenes_a_cargo = []
        self.conn = conn
    
    def registrar_nene(self, nene):
        self.nenes_a_cargo.append(nene)
        nene.esta_registrado = True
        nene.save()
    
    def restringir_lista_por_edad(self, nene, edad):
        if self._nene_esta_a_mi_cargo(nene):
            for juguete in nene.juguetes:
                if juguete['edad_recomendada'] > edad:
                    juguete['mostrar'] = False
    
    def aumentar_karma(self, nene, numero=1):
        nene.karma += numero
    
    def disminuir_karma(self, nene, numero=1):
        nene.karma -= numero

    def _nene_esta_a_mi_cargo(self, nene):
        return nene in self.nenes_a_cargo
    
    def crear(self, nene_id):
        with self.conn:    
            sql = f''' INSERT INTO papas(nombre,nene_a_su_cargo)
                    VALUES("{self.nombre}",{nene_id}) '''
            cur = self.conn.cursor()
            cur.execute(sql)
            return cur.lastrowid
    
