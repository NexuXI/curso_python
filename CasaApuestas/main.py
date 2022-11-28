# Import utils
import random
# Import logs
import CasaApuestas.utils.loging as log
# Import Clases
from CasaApuestas.clases.caballos import Caballo
from CasaApuestas.clases.gran_premio import Gran_premio
from CasaApuestas.clases.apostantes import Apostante
# Import DAO
from CasaApuestas.DAO.caballos_dao import caballosDAO as DAO_caballos
from CasaApuestas.DAO.gran_premio_dao import gran_premioDAO as DAO_gran_premio
from CasaApuestas.DAO.apostantes_dao import apostantesDAO as DAO_apostantes
# Import Lectura
import CasaApuestas.lectura.lectura_caballos as leer_caballos
import CasaApuestas.lectura.lectura_gran_premio as leer_gran_premio
import CasaApuestas.lectura.lectura_apostantes as leer_apostantes
# Import Funciones
from CasaApuestas.functionality.realizar_funciones import *



insertar_en_bd()
gp = DAO_gran_premio.seleccionar_especifico(1)
realizar_gran_premio(gp[0])
