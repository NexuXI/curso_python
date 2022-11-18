# Creacion de la clase padre Doctor que a su vez hereda de Trabajador
import random

from Hospital.Clases.Trabajador import Trabajador


class Doctor(Trabajador):
    def __init__(self, nombre, apellidos, dni, especialidad):
        '''
        :param nombre: Nombre
        :param apellidos: Apellidos
        :param dni: DNI
        :param especialidad: Especialidad
        '''
        Trabajador.__init__(self, nombre, apellidos, dni)
        self.especialidad = especialidad

    def diagnosticar(self, paciente):
        '''
        :param paciente: Objeto paciente al que se le diagnostica.
        :return: Devuelve booleano segun si hay que internar al paciente o no.
        '''
        print(
            f'El doctor {self.nombre} {self.apellidos} esta diagnosticando al paciente: {paciente.nombre} {paciente.apellidos}')
        probabilidad_enfermo = random.randint(0, 10)
        print(
            f'El paciente: {paciente.nombre} {paciente.apellidos} tiene una probabilidad de {probabilidad_enfermo} de estar enfermo sobre 10.')
        if probabilidad_enfermo >= 7:
            print(f'El paciente esta enfermo de gravedad y debe ser internado')
            return True
        else:
            print(f'El paciente ha sido tratado y puede irse a casa')
            return False
