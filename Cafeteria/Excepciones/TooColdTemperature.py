from Proyecto.Cafeteria.Excepciones.TemperatureException import TemperatureException


class TooColdTemperature(TemperatureException):

    def __init__(self):
        super().__init__("El cliente protesta porque el cafe esta frio.")
