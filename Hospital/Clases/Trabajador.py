# Creación de la clase padre Trabajador que a su vez hereda de Persona
import datetime

from Proyecto.Hospital.Clases.Persona import Persona


class Trabajador(Persona):
    def __init__(self, nombre, apellidos, dni):
        """
        :param nombre: Nombre
        :param apellidos: Apellidos
        :param dni: DNI
        """
        Persona.__init__(self, nombre, apellidos, dni)

    def fichar(self):
        """
        Imprime un mensaje de que la persona ha fichado.
        :return: No devuelve nada.
        """
        hora = datetime.datetime.now()
        print(f'El trabajador: {self.nombre} {self.apellidos} ({self.__class__.__name__}) ha fichado a las: [{hora}].')
