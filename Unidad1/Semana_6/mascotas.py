# Clase base: Mascota
class Mascota:
    def __init__(self, nombre, edad):
        self._nombre = nombre        # Atributo encapsulado (encapsulación con "_")
        self._edad = edad            # Otro atributo encapsulado

    def hacer_sonido(self):
        return "Este animal hace un sonido..."

    def mostrar_info(self):
        return f"Nombre: {self._nombre}, Edad: {self._edad} años"


# Clase derivada: Perro (hereda de Mascota)
class Perro(Mascota):
    def __init__(self, nombre, edad, raza):
        super().__init__(nombre, edad)  # Herencia de atributos de Mascota
        self._raza = raza               # Atributo adicional

    # Polimorfismo: sobrescritura del método hacer_sonido
    def hacer_sonido(self):
        return "¡Guau guau!"

    def mostrar_info(self):
        # Polimorfismo usando super() y extendiendo el comportamiento
        return super().mostrar_info() + f", Raza: {self._raza}"


# Clase derivada: Gato (hereda de Mascota)
class Gato(Mascota):
    def __init__(self, nombre, edad, color):
        super().__init__(nombre, edad)
        self._color = color

    def hacer_sonido(self):
        return "¡Miau!"

    def mostrar_info(self):
        return super().mostrar_info() + f", Color: {self._color}"


# Zona de pruebas e instanciación de objetos
if __name__ == "__main__":
    # Crear objetos (instanciación)
    perro1 = Perro("Rex", 5, "Labrador")
    gato1 = Gato("Michi", 3, "Negro")

    # Mostrar la información y sonidos de cada mascota
    print(perro1.mostrar_info())
    print(perro1.hacer_sonido())

    print(gato1.mostrar_info())
    print(gato1.hacer_sonido())
