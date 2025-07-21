# Programa para calcular el promedio semanal del clima usando Programación Orientada a Objetos (POO)

class ClimaSemanal:
    def __init__(self):
        self.__temperaturas = []

    def ingresar_temperaturas(self):
        for i in range(7):
            temp = float(input(f"Ingrese la temperatura del día {i+1}: "))
            self.__temperaturas.append(temp)

    def calcular_promedio(self):
        if not self.__temperaturas:
            return 0
        return sum(self.__temperaturas) / len(self.__temperaturas)

def main():
    print("PROMEDIO SEMANAL DEL CLIMA - POO")
    clima = ClimaSemanal()
    clima.ingresar_temperaturas()
    promedio = clima.calcular_promedio()
    print(f"El promedio semanal de temperaturas es: {promedio:.2f}°C")

if __name__ == "__main__":
    main()
