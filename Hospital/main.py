# Imports
import random

from Clases.Consulta import Consulta
from Clases.Doctor import Doctor
from Clases.Enfermero import Enfermero
from Clases.Hospital import Hospital
from Clases.Paciente import Paciente

# Lista de posibles sintomas
sintomas = ["dolor de cabeza", "nauseas", "tos seca", "poco apetito", "fiebre"]

# Habitaciones vacias
habitaciones = []

# Sala de espera vacia
sala_de_espera = []

# Crear enfermeros
enfermero1 = Enfermero("Salvador", "Domingo", "7777I", "Planta 1")
enfermero2 = Enfermero("Carlota", "Alonso", "2301E", "Planta 2")

# Lista enfermeros
enfermeros = [enfermero1, enfermero2]

# Crear docotres
doctor1 = Doctor("David", "Martinez", "1111A", "Radiologia")
doctor2 = Doctor("Eva", "Fernandez", "2222B", "Cardiologia")

# Lista doctores
doctores = [doctor1, doctor2]

# Consultas
consulta1 = Consulta(1, doctor1)
consulta2 = Consulta(1, doctor2)

# Lista consultas
consultas = [consulta1, consulta2]

# Pacientes
paciente1 = Paciente("Jose", "Garcia", "1234A", random.choice(sintomas))
paciente2 = Paciente("Ana", "Sanchez", "4321B", random.choice(sintomas))
paciente3 = Paciente("Maria", "Hernandez", "1590C", random.choice(sintomas))
paciente4 = Paciente("Miguel", "Rodriguez", "2468F", random.choice(sintomas))

pacientes = [paciente1, paciente2, paciente3, paciente4]

hospital1 = Hospital("Hospital 1", sala_de_espera, habitaciones, consultas)

# Añadir doctores al hospital
for doctor in doctores:
    hospital1.addDoctor(doctor)

# Añadir enfermeros al hospital
for enfermero in enfermeros:
    hospital1.addEnfermero(enfermero)

# Añadir pacientes al hospital
for paciente in pacientes:
    hospital1.addPaciente(paciente)

# Realizar las operaciones del hospital
hospital1.relizar_operaciones()

# Mostrar enfermos que están en las habitaciones
print("-------------Habitaciones--------")
for enfermo in hospital1.habitaciones:
    print(f'{enfermo.nombre} {enfermo.apellidos} con DNI: {enfermo.dni} esta enfermo de: {enfermo.enfermedad}')
