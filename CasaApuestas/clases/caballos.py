import random
from CasaApuestas.utils.loging import log
from datetime import datetime, date


class Caballo:
    def __init__(self, nombre, fecha_nacimiento, velocidad, experiencia,
                 valor_apuesta,
                 id_carrera, id=None):
        self._id = id
        self._nombre = nombre
        self._fecha_nacimiento = fecha_nacimiento
        self._velocidad = velocidad
        self._experiencia = experiencia
        self._valor_apuesta = valor_apuesta
        self._id_carrera = id_carrera

    def __str__(self):
        return f"| {self.nombre}. Valor de apuesta: {self.valor_apuesta} |"

    def todoSTR(self):
        return f"Id: {self.id} Nombre: {self.nombre} Fecha de nacimiento: {self.fecha_nacimiento} Velocidad: {self.velocidad} Experiencia: {self.experiencia} Valor de la apuesta: {self.valor_apuesta} Id de la carrera: {self.id_carrera}"

    @property
    def id(self):
        return self._id

    @id.setter
    def id(self, id):
        self._id = id

    @property
    def nombre(self):
        return self._nombre

    @nombre.setter
    def nombre(self, nombre):
        self._nombre = nombre

    @property
    def fecha_nacimiento(self):
        return self._fecha_nacimiento

    @fecha_nacimiento.setter
    def fecha_nacimiento(self, fecha_nacimiento):
        self._fecha_nacimiento = fecha_nacimiento

    @property
    def velocidad(self):
        return self._velocidad

    @velocidad.setter
    def velocidad(self, velocidad):
        self._velocidad = velocidad

    @property
    def experiencia(self):
        return self._experiencia

    @experiencia.setter
    def experiencia(self, experiencia):
        self._experiencia = experiencia

    @property
    def valor_apuesta(self):
        return self._valor_apuesta

    @valor_apuesta.setter
    def valor_apuesta(self, valor_apuesta):
        self._valor_apuesta = valor_apuesta

    @property
    def id_carrera(self):
        return self._id_carrera

    @id_carrera.setter
    def id_carrera(self, id_carrera):
        self._id_carrera = id_carrera

    def correr(self):
        today = date.today()
        edad = today.year - self.fecha_nacimiento.year - ((today.month, today.day) < (self.fecha_nacimiento.month, self.fecha_nacimiento.day))
        # birthday = date(self.fecha_nacimiento.year, self.fecha_nacimiento.month, self.fecha_nacimiento.day)
        # datetime.date(YEAR,MONTH,DAY)
        # now = date.today()
        # delta = now - birthday
        #edad = delta.days
        cantidad_avanzada = self.velocidad + self.experiencia - edad + random.randint(1, 50)
        # log.debug(cantidad_avanzada)
        return cantidad_avanzada
