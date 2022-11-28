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


def insertar_en_bd():
    grandes_premios_leidos = leer_gran_premio.leer_archivo()
    for gran_premio in grandes_premios_leidos:
        gp = Gran_premio(gran_premio.nombre, gran_premio.distancia, gran_premio.num_carreras)
        DAO_gran_premio.insertar(gp)

    caballos_leidos = leer_caballos.leer_archivo()
    for caballo in caballos_leidos:
        cb = Caballo(caballo.nombre, caballo.fecha_nacimiento, caballo.velocidad, caballo.experiencia,
                     caballo.valor_apuesta, caballo.id_carrera)
        DAO_caballos.insertar(cb)

    apostantes_leidos = leer_apostantes.leer_archivo()
    for apostante in apostantes_leidos:
        ap = Apostante(apostante.nombre, apostante.saldo)
        DAO_apostantes.insertar(ap)


def sacar_objetos():
    objetos = {}
    gps = DAO_gran_premio.seleccionar()
    aps = DAO_apostantes.seleccionar()
    cbs = DAO_caballos.seleccionar()
    objetos["caballos"] = cbs
    objetos["grandes_premios"] = gps
    objetos["apostantes"] = aps
    return objetos


def sacar_grandes_premios():
    return DAO_gran_premio.seleccionar()


def sacar_caballos():
    return DAO_caballos.seleccionar()


def sacar_apostantes():
    return DAO_apostantes.seleccionar()


def realizar_vuelta(gran_premio):
    caballos = DAO_caballos.seleccionar_carrera(gran_premio)
    distancia = gran_premio.distancia
    distancias_caballos = {}
    for index, caballo in enumerate(caballos):
        distancia_recorrida = 0
        while distancia_recorrida < distancia:
            distancia_recorrida += caballo.correr()
        distancias_caballos[caballo.nombre] = distancia_recorrida
        log.debug(f"El caballo: {caballo.nombre} ha recorrido una distancia de: {distancia_recorrida}")
    mayor_distancia = 0
    for caballo in caballos:
        distancia_del_caballo = distancias_caballos[caballo.nombre]
        if distancia_del_caballo > mayor_distancia:
            mayor_distancia = distancia_del_caballo
    caballo_ganador = ""
    for caballo in caballos:
        if distancias_caballos[caballo.nombre] == mayor_distancia:
            caballo_ganador = caballo.nombre
            log.debug(f"El ganador de la carrera es: {caballo.nombre}")
    for caballo in caballos:
        if caballo.nombre == caballo_ganador:
            caballo.experiencia += 5
        else:
            caballo.experiencia += 1

        DAO_caballos.actualizar_experiencia(caballo)
    caballos = DAO_caballos.seleccionar()
    leer_caballos.escribir_archivo(caballos)
    return caballo_ganador


def realizar_carrera_con_apuestas(gran_premio):
    caballos = DAO_caballos.seleccionar_carrera(gran_premio)
    objetos = sacar_objetos()
    apostantes = objetos["apostantes"]
    apuestas = {}
    for apostante in apostantes:
        log.debug("Eliga a quien quiere apostar:")
        for caballo in caballos:
            log.debug(caballo)
        caballo_elegido = random.choice(caballos)
        cantidad_apostada = apostante.apostar()
        log.debug(f"El apostante: {apostante.nombre} ha apostado {cantidad_apostada} por: {caballo_elegido}.")
        apuestas[apostante.id] = [caballo_elegido, cantidad_apostada]
    caballo_ganador = realizar_vuelta(gran_premio)
    for apostante in apostantes:
        apuesta_persona = apuestas[apostante.id]
        if apuesta_persona[0].nombre == caballo_ganador:
            apostante.saldo += apuesta_persona[1] * apuesta_persona[0].valor_apuesta
        DAO_apostantes.actualizar(apostante)
    leer_apostantes.escribir_archivo(apostantes)


def realizar_gran_premio(gran_premio):
    vueltas = gran_premio.num_carreras
    for vuelta in range(vueltas):
        realizar_carrera_con_apuestas(gran_premio)
    caballos = DAO_caballos.seleccionar_carrera(gran_premio)
    apostantes = DAO_apostantes.seleccionar()
    log.debug("-------------Estadísticas de los caballos-------------")
    for caballo in caballos:
        log.debug(f"Nombre:{caballo.nombre}|Experiencia:{caballo.experiencia}|Velocidad:{caballo.velocidad}|Valor de la apuesta:{caballo.valor_apuesta}")
    log.debug("-------------Estadísticas de los apostantes-------------")
    for apostante in apostantes:
        log.debug(f"Nombre:{apostante.nombre}|Saldo:{apostante.saldo}")




