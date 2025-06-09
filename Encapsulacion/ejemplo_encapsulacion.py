# ejemplo_encapsulacion.py

# Ejemplo de encapsulación: clase CuentaBancaria con atributos privados

class CuentaBancaria:
    def __init__(self, saldo_inicial):
        self.__saldo = saldo_inicial  # Atributo privado

    def depositar(self, cantidad):
        if cantidad > 0:
            self.__saldo += cantidad
            print(f"Depósito exitoso. Saldo actual: {self.__saldo}")
        else:
            print("El monto debe ser positivo.")

    def retirar(self, cantidad):
        if 0 < cantidad <= self.__saldo:
            self.__saldo -= cantidad
            print(f"Retiro exitoso. Saldo actual: {self.__saldo}")
        else:
            print("Fondos insuficientes o monto inválido.")

# Uso del ejemplo
mi_cuenta = CuentaBancaria(100)
mi_cuenta.depositar(50)
mi_cuenta.retirar(30)
