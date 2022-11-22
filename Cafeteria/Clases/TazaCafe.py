class TazaCafe:
    def __init__(self, temperatura, tipo_cafe):
        self.temperatura = temperatura
        self.tipo_cafe = tipo_cafe

    def __str__(self):
        return "Un cafe {} a temperatura de {}.".format(self.tipo_cafe, self.temperatura)