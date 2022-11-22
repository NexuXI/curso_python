import Proyecto.utils.loging as log

from Proyecto.Cafeteria.Clases.Persona import Persona


class Cliente(Persona):

    def tomarTazaCafe(self, tazaCafe):
        #logging.debug("El cliente se toma la taza de cafe.")
        log.debug(f"el cliente se toma la taza de cafe {tazaCafe.tipo_cafe}.")
