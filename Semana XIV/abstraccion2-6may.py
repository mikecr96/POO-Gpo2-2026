from abc import ABC, abstractmethod

# Esta es la clase abstracta, en ella definimos el QUÉ hacer
class CuentaBancaria(ABC):
    def __init__(self, titular:str, saldo=0):
        self.titular = titular
        self._saldo = saldo

    @property
    def saldo(self):
        return self._saldo
    
    @saldo.setter
    def saldo(self, saldo):
        if saldo < 0:
            raise ValueError("El saldo no puede ser negativo.")
        self._saldo = saldo

    @saldo.deleter
    def saldo(self):
        print("La cuenta fue reiniciada.")
        self._saldo = 0

    @abstractmethod
    def retirar(self, cantidad): pass

    @abstractmethod
    def descripcion(self): pass

class CuentaAhorro(CuentaBancaria):
    def retirar(self, cantidad):
        if cantidad < 0:
            raise ValueError("No puedes retirar cantidades negativas. $%#$#$#$")
        elif self.saldo < cantidad:
            raise ValueError("La cantidad no puede ser mayor que tu saldo.")
        else:
            self.saldo -= cantidad # Le estamos hablando al setter
            print(f"Retiraste ${cantidad} de tu cuenta. Saldo disponible: ${self.saldo}")

    def descripcion(self):
        print(f"Hola, {self.titular}, buen día. Tu cuenta de ahorro tiene ${self.saldo} disponible.")


# Función concreta
def pagar(cuenta, monto):
    pass
# Luego vemos para qué sirve, pero es algo muy común en scripts de python
if __name__ == "__main__":
    c1 = CuentaAhorro("Miguel", 1000)
    c1.descripcion()
    c1.retirar(-10)