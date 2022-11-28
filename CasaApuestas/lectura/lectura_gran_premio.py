from os import remove
import CasaApuestas.utils.loging as log
from CasaApuestas.clases.gran_premio import Gran_premio

NOMBRE = 0
DISTANCIA = 1
NUM_CARRERAS = 2
SEPARADOR_DATOS = "|"


def leer_archivo():
    grandes_premios = []
    log.debug("Empezando a leer el archivo")
    with open('../files/grandes_premios.txt', 'r', encoding='utf8') as archivo:
        for linea in archivo:
            log.debug(linea)
            datos = linea.split(SEPARADOR_DATOS)
            for dato in datos:
                if "\n" in dato:
                    dato.replace("\n", "")
            gran_premio = Gran_premio(datos[NOMBRE], datos[DISTANCIA], datos[NUM_CARRERAS])
            grandes_premios.append(gran_premio)
    return grandes_premios


def escribir_archivo(grandes_premios):
    remove('../files/grandes_premios.txt')
    nombre_archivo = "../files/grandes_premios.txt"
    archivo = open(nombre_archivo, 'x', encoding='utf8')
    archivo.close()
    file = open(nombre_archivo, "w", encoding='utf8')
    for gran_premio in grandes_premios:
        texto = gran_premio.nombre + "|" + gran_premio.distancia + "|" + gran_premio.num_carreras + "\n"
        file.write(texto)
    file.close()
