import logging as log
import random
from abc import ABC
from Orquestra.Exceptions.exceptions import FineTuneException

log.basicConfig(level=log.DEBUG,
                format='%(asctime)s: %(levelname)s [%(filename)s:%(lineno)s] %(message)s',
                datefmt='%I:%M:%S %p',
                handlers=[
                    log.FileHandler('../logs/orquestra.log'),
                    log.StreamHandler()
                ])


def decorador (funcion_a_decorar):
    def funcion_decorador(*args):
        log.debug("Antes de la ejecución de la funcion")
        resultado = funcion_a_decorar(*args)
        log.debug("Después de la ejecución de la funcion")
        return resultado

    return funcion_decorador


class Instrumento(ABC):
    def __init__(self, nombre, tipo):
        self._afinado = False
        self.nombre = nombre
        self.tipo = tipo

    @property
    def afinado(self):
        return self._afinado

    @afinado.setter
    def afinado(self, afinado):
        self._afinado = afinado

    def __str__(self):
        return "Instrumento: {}, de tipo: {}".format(self.nombre, self.tipo)

    @decorador
    def afinar(self):
        self.afinado = random.choice([True, False])
        log.info(f"Instrumento {self.nombre} esta: {self.afinado}")

    @decorador
    def tocar(self):
        if self.afinado:
            return self.__str__(), " se esta tocando de manera correcta."
        else:
            raise FineTuneException(f"Instrumento: {self.nombre} no afinado.")


class Guitarra(Instrumento):
    def __init__(self, nombre, tipo, num_cuerdas):
        super().__init__(nombre, tipo)
        self.num_cuerdas = num_cuerdas


class GuitarraElectrica(Guitarra):
    def __init__(self, nombre, tipo, num_cuerdas, potencia):
        super().__init__(nombre, tipo, num_cuerdas)
        self.potencia = potencia


class Tambor(Instrumento):
    def __init__(self, nombre, tipo, size):
        super().__init__(nombre, tipo)
        self.size = size

    def aporrear(self):
        if self.afinado:
            return self.__str__(), " se esta tocando de manera correcta."
        else:
            raise FineTuneException(f"Instrumento: {self.nombre} no afinado.")


class Piano(Instrumento):
    def __init__(self, nombre, tipo, num_teclas):
        super().__init__(nombre, tipo)
        self.num_cuerdas = num_teclas


class Orquestra:

    def __init__(self):
        self._instrumentos = None

    @property
    def instrumentos(self):
        return self._instrumentos

    @instrumentos.setter
    def instrumentos(self, instrumentos):
        self._instrumentos = instrumentos

    def crear_orquestra(self, guitarra, guitarra_electrica, piano, tambor):
        self._instrumentos = [guitarra, guitarra_electrica, piano, tambor]

    def iniciar_concierto(self):
        map(lambda x: x.afinar(), self.instrumentos)
        log.debug("Instrumentos afinados.")
        for instrumento in self.instrumentos:
            while not instrumento.afinado:
                try:
                    if isinstance(instrumento, Tambor):
                        log.debug(instrumento.aporrear())
                    else:
                        log.debug(instrumento.tocar())
                except FineTuneException as ftex:
                    log.error(ftex)
                    instrumento.afinar()
        log.debug("Inicia el concierto.")
        for instrumento in self.instrumentos:
            if instrumento.afinado:
                log.debug(f"{instrumento.nombre} esta afinado")
                if isinstance(instrumento, Tambor):
                    log.debug(instrumento.aporrear())
                else:
                    log.debug(instrumento.tocar())
        log.debug("El concierto ha terminado.")