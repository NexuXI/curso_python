import Proyecto.utils.loging as log

from Proyecto.Cafeteria.Excepciones.TemperatureException import TemperatureException
from Proyecto.Cafeteria.Excepciones.TooColdTemperature import TooColdTemperature
from Proyecto.Cafeteria.Excepciones.TooHotTemperature import TooHotTemperature


class Bar:
    def __init__(self,):
        self.camarero = None
        self.cliente = None

    def operar(self):
        try:
            tipo_cafe = input("tipo de cafe que desea. ")
            log.debug(f"El camarero: {self.camarero} está sirviendo al cliente: {self.cliente}.")
            taza_cafe = self.camarero.servirTazaCafe(tipo_cafe)
            log.debug(taza_cafe)
            self.cliente.tomarTazaCafe(taza_cafe)
            if taza_cafe.temperatura > 80 or taza_cafe.temperatura < 20:
                if taza_cafe.temperatura > 80:
                    raise TooHotTemperature()
                elif taza_cafe.temperatura < 20:
                    raise TooColdTemperature()
                else:
                    raise TemperatureException('Problema en la temperatura de la taza de cafe.')
        except Exception as e:
            log.warn(f'Exception - Ocurrió un error: {e} , {type(e)}')
        else:
            log.debug('El cafe estaba a una temperatura aceptable.')

