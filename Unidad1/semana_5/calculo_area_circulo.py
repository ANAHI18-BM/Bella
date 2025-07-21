# Programa: Calculadora de Áreas (Círculo y Cuadrado)
# Descripción: Este programa permite al usuario calcular el área de un círculo o un cuadrado según su elección.
# Autor: Bella Morocho
# Fecha: 29 de junio de 2025
# Este código demuestra el uso de tipos de datos, condicionales, identificadores descriptivos y documentación en Python.

import math  # Para usar el valor de pi

# Mostrar menú de opciones
print("=== Calculadora de Áreas ===")
print("1. Calcular área de un círculo")
print("2. Calcular área de un cuadrado")
opcion = input("Seleccione una opción (1 o 2): ")

# Convertir opción a número entero
opcion = int(opcion)

if opcion == 1:
    # Área de un círculo
    radio_str = input("Ingrese el radio del círculo en cm: ")
    radio = float(radio_str)
    if radio > 0:
        area_circulo = math.pi * radio ** 2
        print(f"El área del círculo es {area_circulo:.2f} cm²")
    else:
        print("Error: El radio debe ser un número positivo.")
elif opcion == 2:
    # Área de un cuadrado
    lado_str = input("Ingrese el lado del cuadrado en cm: ")
    lado = float(lado_str)
    if lado > 0:
        area_cuadrado = lado * lado
        print(f"El área del cuadrado es {area_cuadrado:.2f} cm²")
    else:
        print("Error: El lado debe ser un número positivo.")
else:
    print("Opción inválida. Por favor seleccione 1 o 2.")
