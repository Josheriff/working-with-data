from dummy_data import nombre_adulto, nombre_nene, edad_nene, juguetes
from papas import Papa
from nenes import Nene


papa = Papa(nombre_adulto)
nene = Nene(nombre_nene, edad_nene, juguetes)

papa.registrar_nene(nene)
papa.restringir_lista_por_edad(nene, 10)

nene.mostrar_lista()

