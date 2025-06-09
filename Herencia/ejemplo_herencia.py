# ejemplo_herencia.py

# Ejemplo de herencia: clase Animal y subclase Perro

class Animal:
    def __init__(self, nombre):
        self.nombre = nombre

    def hablar(self):
        print("Este animal hace un sonido.")

class Perro(Animal):
    def hablar(self):
        print(f"{self.nombre} dice: ¡Guau!")

# Uso del ejemplo
mi_perro = Perro("Max")
mi_perro.hablar()
