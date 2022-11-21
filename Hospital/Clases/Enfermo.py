# Creación de la clase Enfermo que hereda de Persona
from Proyecto.Hospital.Clases.Persona import Persona


class Enfermo(Persona):
    def __init__(self, nombre, apellidos, dni, enfermedad):
        """
        :param nombre: Nombre.
        :param apellidos: Apellidos.
        :param dni: DNI.
        :param enfermedad: Enfermedad.
        """
        Persona.__init__(self, nombre, apellidos, dni)
        self.enfermedad = enfermedad
