# Abstract Basic Class
from abc import ABC, abstractmethod


class Persona(ABC):
    def __init__(self, nombre):
        self.nombre = nombre

    def __str__(self):
        return "Nombre: {}".format(self.nombre)
