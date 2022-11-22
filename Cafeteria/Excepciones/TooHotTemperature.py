from Proyecto.Cafeteria.Excepciones.TemperatureException import TemperatureException


class TooHotTemperature(TemperatureException):

    def __init__(self):
        super().__init__("El cliente se ha quemado la lengua")
