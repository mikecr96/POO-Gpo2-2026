from abc import ABC, abstractmethod

# Esto no es común, de hecho, no lo recomiendo
# __name__ = "Personaje"

class Personaje(ABC):
    @abstractmethod
    def atacar(self, tipo:str):
        pass

class Guerrero(Personaje):
    def atacar(self, tipo:str):
        print(f"El guerrero ataca usando: {tipo}.")

class Mago(Personaje):
    def atacar(self, tipo:str):
        print(f"El mago ataca usando: {tipo}.")

def presionar_X(personaje:Personaje|Guerrero|Mago, tipo:str):
    personaje.atacar(tipo)

if __name__ == "__main__":
    print(__name__)
    j1 = Guerrero()
    j2 = Mago()    
    print("El jugador presionó el botón x")
    presionar_X(j1, "Hachazo")
    print("El jugador presionó el botón x")
    presionar_X(j2, "Lanzarayos")