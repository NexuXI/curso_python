import os

from Colegio.clases import Colegio, Alumno

colegios = []
numeros_colegio = []
alumnos = []

# De manera automática abre y cierra el archivo no hace falta try catch
with open('alumnos-colegio.txt', 'r', encoding='utf8') as archivo:
    lineas = archivo.readlines()
    for linea in lineas:
        if "Colegio" in linea:
            if not linea[7] in numeros_colegio:
                numeros_colegio.append(linea[7])

    for numero in numeros_colegio:
        nombre_colegio = numero
        colegios.append(Colegio(nombre_colegio))

    for colegio in colegios:
        nombre_lista = "Alumnos", colegio.nombre
        nom = "".join([str(_) for _ in nombre_lista])
        valor_lista = []
        dict1 = {nom: valor_lista}
        alumnos.append(dict1)

    for linea in lineas:
        for colegio in colegios:
            if colegio.nombre == linea[7]:
                elementos = linea.split("|")
                asignaturas = elementos[4].split(";")
                asignaturas_final = []
                for asignatura in asignaturas:
                    asignaturas_final.append(asignatura.replace("\n", ""))
                alumno = Alumno(elementos[1], elementos[2], elementos[3], asignaturas_final)
                for diccionario in alumnos:
                    llaves = diccionario.keys()
                    for llave in llaves:
                        if colegio.nombre in llave:
                            diccionario[llave].append(alumno)

    for colegio in colegios:
        for elemento in alumnos:
            for p in elemento.values():
                for al in p:
                    colegio.alumnos.append(al)

    for colegio in colegios:
        nombre_archivo = "Colegio", colegio.nombre
        nom = "".join([str(_) for _ in nombre_archivo])
        nom = nom + ".txt"
        if not os.path.exists(nom):
            archivo = open(nom, 'x', encoding='utf8')
            archivo.close()
        file = open(nom, "w", encoding='utf8')
        for elemento in alumnos:
            for p in elemento.values():
                for al in p:
                    texto = al.nombre + "|" + al.apellido + "|" + al.dni + "|"
                    for asignatura in al.asignaturas:
                        texto += asignatura + ";"
            texto_final = "".join([str(_) for _ in nombre_archivo])+"|"+texto.rstrip(texto[-1])
            file.write(texto_final + "\n")
        file.close()


