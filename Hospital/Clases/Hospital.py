from Hospital.Clases.Enfermo import Enfermo


class Hospital:
    def __init__(self, nombre, sala_de_espera, habitaciones, consultas, doctores=[], enfermeros=[]):
        '''
        :param nombre: Nombre del hospital.
        :param sala_de_espera: Lista con los pacientes.
        :param habitaciones: Lista con los enfermos.
        :param consultas: Lista con Objetos Consulta.
        :param doctores: Lista con Objetos Doctor.
        :param enfermeros: Lista con Objetos Enfermero.
        '''
        self.nombre = nombre
        self.consultas = consultas
        self.doctores = doctores
        self.enfermeros = enfermeros
        self.sala_de_espera = sala_de_espera
        self.habitaciones = habitaciones

    def addDoctor(self, doctor):
        '''
        Metodo que sirve para añadir un doctor a la lista de doctores
        :param doctor: Recibe un objeto Doctor
        :return: no devuelve nada
        '''
        self.doctores.append(doctor)

    def addEnfermero(self, enfermero):
        '''
        Metodo que sirve para añadir un enfermero a la lista de enfermeros.
        :param enfermero: Recibe un objeto Enfermero
        :return: No devuelve nada
        '''
        self.enfermeros.append(enfermero)

    def addPaciente(self, paciente):
        '''
        Metodo que sirve para añadir un paciente a la sala de espera.
        :param paciente: Recibe un objeto Paciente
        :return: No devuelve nada
        '''
        self.sala_de_espera.append(paciente)

    def addEnfermo(self, enfermo):
        '''
        Metodo que sirve para añadir un enfermo a las habitaciones.
        :param enfermo: Recibe un objeto Enfermo
        :return: No devuelve nada
        '''
        self.habitaciones.append(enfermo)

    def relizar_operaciones(self):
        '''
        Realiza todas las operaciones de fichado, atender a los pacientes, diagnositcarlos, internarlos sin son enfermos y si no caben mandarlos a otro hospital.
        :return: No devuelve nada
        '''
        print("------------------------------------------------------")
        print("Fichas de entrada")
        for consulta in self.consultas:
            consulta.doctor.fichar()
        for enfermero in self.enfermeros:
            enfermero.fichar()
        print("------------------------------------------------------")
        while len(self.sala_de_espera) != 0:
            for enfermero in self.enfermeros:
                for paciente in self.sala_de_espera:
                    print("--> --> --> --> --> --> --> --> --> --> --> --> --> --> --> ")
                    enfermero.atender(paciente, self.consultas)
                    self.sala_de_espera.pop(0)
                    for consulta in self.consultas:
                        if consulta.doctor.diagnosticar(paciente):
                            # Esta enfermo de gravedad
                            enfermedades = ["Cancer", "VIH", "Hepatitis", "Leucemia", "COVID-19"]
                            enfermedad = ""
                            match paciente.sintomas:
                                case "dolor de cabeza":
                                    enfermedad = enfermedades[0]
                                case "nauseas":
                                    enfermedad = enfermedades[1]
                                case "tos seca":
                                    enfermedad = enfermedades[2]
                                case "poco apetito":
                                    enfermedad = enfermedades[3]
                                case "fiebre":
                                    enfermedad = enfermedades[4]
                                case _:
                                    enfermedad = "Enfermedad muy rara"
                            enfermo = Enfermo(paciente.nombre, paciente.apellidos, paciente.dni, enfermedad)
                            # Borra paciente tras crear enfermo
                            print(f'Paciente de la consulta: {paciente.nombre}')
                            consulta.removePaciente()
                            if len(self.habitaciones) < 3:
                                print(
                                    f'El paciente: {paciente.nombre} {paciente.apellidos} ha sido internado como enfermo en una de las habitaciones.')
                                self.addEnfermo(enfermo)
                                for pac in self.sala_de_espera:
                                    if pac == paciente:
                                        del pac

                            else:
                                print("Las habitaciones estan llenas y el enfermo ha sido trasladado a otro hospital")
                                for pac in self.sala_de_espera:
                                    if pac == paciente:
                                        del pac

                        else:
                            # No esta enfermo de gravedad
                            print(f'Paciente de la consulta: {paciente.nombre}')
                            consulta.removePaciente()
                            for pac in self.sala_de_espera:
                                if pac == paciente:
                                    del pac
                    break

        print("------------------------------------------------------")
        print("Fichas de salida")
        for consulta in self.consultas:
            consulta.doctor.fichar()
        for enfermero in self.enfermeros:
            enfermero.fichar()
        print("------------------------------------------------------")
