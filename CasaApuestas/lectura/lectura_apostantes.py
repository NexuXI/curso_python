from os import remove
import CasaApuestas.utils.loging as log
from CasaApuestas.clases.apostantes import Apostante

NOMBRE = 0
SALDO = 1
SEPARADOR_DATOS = "|"


def leer_archivo():
    apostantes = []
    log.debug("Empezando a leer el archivo")
    with open('../files/apostantes.txt', 'r', encoding='utf8') as archivo:
        for linea in archivo:
            # print(linea)
            log.debug(linea)
            datos = linea.split(SEPARADOR_DATOS)
            for dato in datos:
                dato.replace("\n", "")
            apostante = Apostante(datos[NOMBRE], datos[SALDO])
            apostantes.append(apostante)
    return apostantes


def escribir_archivo(apostantes):
    remove('../files/apostantes.txt')
    nombre_archivo = "../files/apostantes.txt"
    archivo = open(nombre_archivo, 'x', encoding='utf8')
    archivo.close()
    file = open(nombre_archivo, "w", encoding='utf8')
    for apostate in apostantes:
        texto = f"{apostate.nombre}|{apostate.saldo}\n"
        file.write(texto)
    file.close()
