from Proyecto.Cafeteria.Clases.Bar import Bar
from Proyecto.Cafeteria.Clases.Camarero import Camarero
from Proyecto.Cafeteria.Clases.Cliente import Cliente

cliente1 = Cliente("Jose")

camarero1 = Camarero("Miguel")

bar1 = Bar()

bar1.cliente = cliente1
bar1.camarero = camarero1

bar1.operar()
