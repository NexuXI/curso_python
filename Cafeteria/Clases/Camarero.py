import random
from Proyecto.Cafeteria.Clases.Persona import Persona
from Proyecto.Cafeteria.Clases.TazaCafe import TazaCafe


class Camarero(Persona):

    def servirTazaCafe(self, tipo_cafe):
        temperatura = random.randint(0, 100)
        cafe = TazaCafe(temperatura, tipo_cafe)
        return cafe
