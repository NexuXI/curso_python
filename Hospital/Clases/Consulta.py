# Creación de la clase Hospital.
from Hospital.Clases.Paciente import Paciente


class Consulta:

    def __init__(self, numero, doctor):
        """
        :param numero: Número de la consulta.
        :param doctor: Doctor asignado.
        """
        self.numero = numero
        self.doctor = doctor
        self.paciente = ""

    def addDoctor(self, doctor):
        """
        Añadir un doctor a la consulta.
        :param doctor: Objeto Doctor.
        :return: No devuelve nada.
        """
        self.doctor = doctor
        self.doctor.fichar()

    def addPaciente(self, paciente):
        """
        Añadir un paciente a la lista de pacientes.
        :param paciente: Objeto Paciente que se añade a la lista.
        :return: No devuelve nada.
        """
        self.paciente = paciente

