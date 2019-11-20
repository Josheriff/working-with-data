from scripts.dummy_data import nombre_adulto, nombre_nene, edad_nene, juguetes
from papas import Papa
from nenes import Nene
from database import create_connection

conn = create_connection()
nene_data = {'nombre':nombre_nene,
             'edad' :edad_nene,
             'juguetes': juguetes}
nene = Nene(nene_data, conn)
nene.crear()
papa = Papa(nombre_adulto, conn)
papa.registrar_nene(nene)


# papa.registrar_nene(nene)
# papa.restringir_lista_por_edad(nene, 10)



# nene.mostrar_lista()
# papa.aumentar_karma(nene,8)
# print('-------------------------')
nene.mostrar_lista()

