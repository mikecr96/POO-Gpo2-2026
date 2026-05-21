# class Camara: 
#     def tomar_foto(self):
#         print(f"Foto tomada 📸")

#     def guardar_en_memoria(self):
#         print("La cámara guardó una foto en memoria")

# class Telefono: 
#     def llamar(self, destino:int):
#         print(f"Haciendo llamda a {destino}")

#     def guardar_en_memoria(self):
#         print("El teléfono guardó un contacto en memoria")

# # Herencia múltiple
# class Smartphone(Camara, Telefono): pass

# if __name__ == "__main__":
#     print(Smartphone.mro())
#     iphone = Smartphone()
#     iphone.tomar_foto()
#     iphone.llamar(5512345678)
#     iphone.guardar_en_memoria()

# class Padre:
#     def dar_permiso(self):
#         print("Pregúntale a tu mamá")

# class Madre:
#     def dar_permiso(self):
#         print("¿Con quién vas?")

# class Hijo(Madre, Padre):
#     def rogar(self):
#         print("El hijo ruega para que lo dejen ir...")

# if __name__ == "__main__":
#     chamaco = Hijo()
#     chamaco.rogar()
#     chamaco.dar_permiso()

# Mixins

# class HabilidadVolarMixin:
#     def volar(self):
#         print("El personaje se eleva por los aires...")

# class PersonajeNormal:
#     def __init__(self, nombre) -> None:
#         self.nombre = nombre

#     def caminar(self):
#         print(f"El personaje {self.nombre} está caminando")

# class SuperHeroe(PersonajeNormal, HabilidadVolarMixin): pass

# # Aquí se crean N cantidad de personajes normales
# if __name__ == "__main__":
#     superman = SuperHeroe('Superman')
#     superman.caminar()
#     superman.volar()

# Problema del diamante

class Base:
    def __init__(self) -> None:
        print("1. LLegamos a Base.")

class ClaseA(Base):
    def __init__(self) -> None:
        print("2. Entramos a clase A")
        super().__init__()
        print("3. Saliendo de Clase A")

class ClaseB(Base):
    def __init__(self) -> None:
        print("4. Entramos a clase B")
        super().__init__()
        print("5. Saliendo de clase B")

class ClaseC(ClaseB, ClaseA):
    def __init__(self) -> None:
        print("6. Entramos a clase C")
        super().__init__()
        print("7. Saliendo de clase C")

objetoC = ClaseC()