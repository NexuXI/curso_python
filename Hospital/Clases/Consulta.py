# Creacion de la clase Hospital
class Consulta:

    def __init__(self, numero, doctor, paciente=[]):
        '''
        :param numero: Numero de la consulta.
        :param doctor: Doctor asignado.
        :param paciente: Lista con solo un (1) Objeto Paciente.
        '''
        self.numero = numero
        self.doctor = doctor
        self.paciente = paciente

    def addDoctor(self, doctor):
        '''
        Añadir un doctor a la consulta.
        :param doctor: Objeto Doctor.
        :return: No devuelve nada.
        '''
        self.doctor = doctor
        self.doctor.fichar()

    def addPaciente(self, paciente):
        '''
        Añadir un paciente a la lista de pacientes.
        :param paciente: Objeto Paciente que se añade a la lista.
        :return: No devuelve nada.
        '''
        self.paciente.append(paciente)

    def removePaciente(self):
        '''
        Borrar el paciente[0] de la lista.
        :return: No devuelve nada.
        '''
        self.paciente.pop(0)

    def removeDoctor(self):
        '''
        Fichar y luego borrar el doctor.
        :return: No devuelve nada.
        '''
        self.doctor.fichar()
        self.doctor.pop(0)
