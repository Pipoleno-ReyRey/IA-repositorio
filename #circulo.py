#esfera
import math

class Esfera:

    def __init__(self, radio: float):
        self.radio = radio
        self.area = self.Area()
        self.volumen = self.Volumen()
        self.diametro = self.Diametro()

    def Area(self):
        area = 4 * math.pi * pow(self.radio,2)
        print(f"el area de la esfera es {area}")
        return area
    
    def Volumen(self):
        volumen = (4/3) * math.pi * pow(self.radio, 3)
        print(f"el volumen de la esfera es {volumen}")
        return volumen
    
    def Diametro(self):
        diametro = self.radio * 2
        print(f"el diametro de la esfera es {diametro}")
        return diametro

esfera = Esfera(5)