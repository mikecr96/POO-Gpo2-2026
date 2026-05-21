# Patrones de diseño
# Singleton
class ConexionDB: # (object)
    _instancia = None
    # Método constructor (encargado de reservar espacio en memoria para el obj)
    # __new__ -> __init__
    # NUNCA se hace override al método new
    def __new__(cls):
        # print("Hola mundo desde new")
        # super(ConexionDB, cls)
        if cls._instancia is None:
            cls._instancia = super().__new__(cls) 
        return cls._instancia

    # Método iniciador
    def __init__(self) -> None:
        print("Hola mundo desde el init")
        # self.nombre = nombre

    def conectar(self):
        pass

c1 = ConexionDB()
c2 = ConexionDB()
# Decimos que son iguales, solo si comparten el mismo espacio de memoria
print(c1 == c2)
print(c1)
print(c2)
# print(issubclass(ConexionDB, object))

# p1 = Perro()
# p2 = Perro()

# print(type(p1))
# print(type(p2))

# # Cuando hablamos de objetos
# # Decimos que son iguales, solo si comparten el mismo espacio de memoria
# print(p1 == p2)
# print(p1)
# print(p2)