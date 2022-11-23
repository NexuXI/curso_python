class Colegio:
    def __init__(self, nombre):
        self.nombre = nombre
        self.alumnos = []

    def addAlumno(self, alumno):
        self.alumnos.append(alumno)

    def __str__(self):
        return f"El colegio: {self.nombre}"

class Alumno:
    def __init__(self, nombre, apellido, dni, asignaturas):
        self.nombre = nombre
        self.apellido = apellido
        self.dni = dni
        self.asignaturas = asignaturas

    def __str__(self):
        return f"El alumno: {self.nombre} {self.apellido} con DNI: {self.dni} tiene las asignaturas: {self.asignaturas}"
