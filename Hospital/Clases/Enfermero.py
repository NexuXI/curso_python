# Creación de la clase padre Doctor que a su vez hereda de Trabajador.
from Hospital.Clases.Trabajador import Trabajador


class Enfermero(Trabajador):

    def __init__(self, nombre, apellidos, dni, planta):
        """
        :param nombre: Nombre.
        :param apellidos: Apellidos.
        :param dni: DNI.
        :param planta: Planta.
        """
        Trabajador.__init__(self, nombre, apellidos, dni)
        self.planta = planta

    def atender(self, paciente, consultas):
        """
        Realiza las operaciones de trasladar de la lista de espera a la consulta disponible al paciente que se le
        indique.
        :param paciente: Objeto Paciente que se atiende.
        :param consultas: Lista de Objetos Consultas donde se atienden.
        :return: No devuelve nada.
        """
        print(
            f'El enfermero {self.nombre} {self.apellidos} de la planta {self.planta} esta atendiendo al paciente: {paciente.nombre} {paciente.apellidos}')
        for consulta in consultas:
            if consulta.paciente == "":
                print(f'Consulta:{consulta.numero:-^15}')
                consulta.addPaciente(paciente)
                break
            else:
                print(f'La consulta {consulta.numero} esta ocupada.')
