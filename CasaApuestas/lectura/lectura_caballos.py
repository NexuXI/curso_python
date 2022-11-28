from os import remove
import CasaApuestas.utils.loging as log
from CasaApuestas.clases.caballos import Caballo

NOMBRE = 0
FECHA_NACIMIENTO = 1
VELOCIDAD = 2
EXPERIENCIA = 3
VALOR_APUESTA = 4
ID_CARRERA = 5
SEPARADOR_DATOS = "|"


def leer_archivo():
    caballos = []
    log.debug("Empezando a leer el archivo")
    with open('../files/caballos.txt', 'r', encoding='utf8') as archivo:
        for linea in archivo:
            # print(linea)
            log.debug(linea)
            datos = linea.split(SEPARADOR_DATOS)
            for dato in datos:
                dato.replace("\n", "")
            caballo = Caballo(datos[NOMBRE], datos[FECHA_NACIMIENTO], datos[VELOCIDAD], datos[EXPERIENCIA], datos[VALOR_APUESTA], datos[ID_CARRERA])
            caballos.append(caballo)
    return caballos


def escribir_archivo(caballos):
    remove('../files/caballos.txt')
    nombre_archivo = "../files/caballos.txt"
    archivo = open(nombre_archivo, 'x', encoding='utf8')
    archivo.close()
    file = open(nombre_archivo, "w", encoding='utf8')
    for caballo in caballos:
        texto = f"{caballo.nombre}|{format(caballo.fecha_nacimiento,'%Y-%m-%d')}|{caballo.velocidad}|{caballo.experiencia}|{caballo.valor_apuesta}|{caballo.id_carrera}\n"
        file.write(texto)
    file.close()
