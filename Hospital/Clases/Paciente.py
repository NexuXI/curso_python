# Creación de la clase Paciente que hereda de Persona
from Proyecto.Hospital.Clases.Persona import Persona


class Paciente(Persona):
    def __init__(self, nombre, apellidos, dni, sintomas):
        """
        :param nombre: Nombre.
        :param apellidos: Apellidos.
        :param dni: DNI.
        :param sintomas: Síntomas.
        """
        Persona.__init__(self, nombre, apellidos, dni)
        self.sintomas = sintomas
