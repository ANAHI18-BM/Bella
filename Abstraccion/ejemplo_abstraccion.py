# ejemplo_abstraccion.py

# Ejemplo de abstracción: clase abstracta Vehiculo y sus métodos

from abc import ABC, abstractmethod

class Vehiculo(ABC):
    @abstractmethod
    def encender(self):
        pass

    @abstractmethod
    def apagar(self):
        pass

class Auto(Vehiculo):
    def encender(self):
        print("El auto está encendido.")

    def apagar(self):
        print("El auto está apagado.")

# Uso del ejemplo
mi_auto = Auto()
mi_auto.encender()
mi_auto.apagar()
