from dummy_data import nombre_adulto, nombre_nene, edad_nene
from papas import Papa

papa = Papa(nombre_adulto)
papa.registrar_nene(nombre_nene, edad_nene)
nenes = papa.nenes_a_cargo
nene = nenes[0]
print(nene)