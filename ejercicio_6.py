class Vehiculo():
    def __init__(self,color,ruedas,puertas):
        self.color = color
        self.ruedas = ruedas
        self.puertas = puertas
    def estado(self):
        print("color: ",self.color,"\nRuedas: ",self.ruedas,"\nPuertas: ",self.puertas)
    
        
class Coche(Vehiculo):
    velocidad = ""
    cilindrada = ""
    def caracteristicas_coche(self):
        self.velocidad = "220km/h"
        self.cilindrada = "8 cilindros en V"
    def estado(self):
        print("\nCaracteristicas del coche \n\ncolor: ",self.color,"\nRuedas: ",self.ruedas,"\nPuertas: ",self.puertas, "\nVelocidad: ",self.velocidad,"\nCilindrada: ",self.cilindrada)
    
    
    
miCoche = Coche("Azul",4,4)
miCoche.caracteristicas_coche()
miCoche.estado()

class Limusina(Vehiculo):
    velocidad = ""
    cilindrada = ""
    def caracteristicas_limusina(self):
        self.velocidad = "120km/h"
        self.cilindrada = "4 cilindros"
    def estado(self):
        print("\nCaracteristicas de la limusina \n\ncolor: ",self.color,"\nRuedas: ",self.ruedas,"\nPuertas: ",self.puertas, "\nVelocidad: ",self.velocidad,"\nCilindrada: ",self.cilindrada)
        
miLimusina = Limusina("Blanco",6,6)
miLimusina.caracteristicas_limusina()
miLimusina.estado()
