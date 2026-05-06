from abc import ABC, abstractmethod

# Clase abstracta es un molde y sirve para definir QUÉ hacer
class CuentaBancaria(ABC):
    def __init__(self, titular:str, saldo=0) -> None:
        self.titular = titular
        self._saldo = saldo

    @property
    def saldo(self):
        return self._saldo
    
    @saldo.setter
    def saldo(self, saldo):
        if saldo < 0:
            raise ValueError("No puedes tener saldo negativo.")
        self._saldo = saldo

    @abstractmethod
    def retirar(self, monto):
        pass # Regla: los métodos abstractos van "vacíos"

    @abstractmethod
    def describir(self):
        pass

class CuentaAhorro(CuentaBancaria):
    # Es OBLIGATORIO sobreescribir los métodos abstractos
    def retirar(self, monto):
        if monto < 0:
            raise ValueError("No puedes retirar montos negativos $%&#.")
        elif self.saldo >= monto:
            self.saldo -= monto
            print(f"Retiro realizado por ${monto}.\nSaldo dispinible: ${self.saldo}")        
        else:
            raise ValueError("No puedes retirar dinero que no tienes")
        
    def describir(self):
        print(f"Buen día {self.titular}.\nSaldo disponible: ${self.saldo}")

class TarjetaCredito(CuentaBancaria):
    def __init__(self, titular: str, lim_cred:float, saldo=0) -> None:
        super().__init__(titular, saldo)
        self.lim_cred = lim_cred
        self.cred_actual = lim_cred

    def retirar(self, monto):
        if monto < 0:
            raise ValueError("No puedes retirar montos negativos $%&#.")
        elif self.cred_actual + self.saldo >= monto:
            if self.saldo >= monto:
                self.saldo -= monto
                print(f"Retiro de {monto} realizado.\nSaldo: {self.saldo}")
            else:
                self.cred_actual -= monto - self.saldo
                self.saldo = 0
                print(f"Retiro de {monto} realizado.\nSaldo: {self.saldo} y crédito disponible de {self.cred_actual}")
        else:
            raise ValueError("No puedes retirar dinero que no tienes. Y no te vamos a prestar tanto.")
        
    def describir(self):
        print(f"buen día {self.titular}.\nSu tarjeta de crédito tiene saldo dispinble de ${self.saldo} y un límite de crédito de ${self.lim_cred}\ny un crédito disponible de ${self.cred_actual}")

# Método externo que las "linkea"
def procesar_retiro(cuenta: TarjetaCredito | CuentaAhorro, monto):
    cuenta.retirar(monto)

if __name__ == "__main__":
    ca1 = CuentaAhorro("Miguel", 1000)
    ca1.describir()
    procesar_retiro(ca1, 1000)
    print("CRÉDITO".center(60, '*'))
    tc1 = TarjetaCredito("Oscar", 2000, 100)
    tc1.describir()
    procesar_retiro(tc1, 1500)