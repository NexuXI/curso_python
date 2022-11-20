# Creación de la clase padre Persona
class Persona:
    def __init__(self, nombre="", apellidos="", dni=""):
        """
        :param nombre: Nombre.
        :param apellidos: Apellidos.
        :param dni: DNI.
        """
        self.nombre = nombre
        self.apellidos = apellidos
        self.dni = dni
