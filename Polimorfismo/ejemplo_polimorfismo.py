# ejemplo_polimorfismo.py

# Ejemplo de polimorfismo: diferentes animales que hacen sonidos

class Gato:
    def hablar(self):
        print("El gato dice: Miau")

class Perro:
    def hablar(self):
        print("El perro dice: Guau")

def hacer_hablar(animal):
    animal.hablar()

# Uso del ejemplo
gato = Gato()
perro = Perro()

hacer_hablar(gato)
hacer_hablar(perro)
