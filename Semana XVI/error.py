diccionario = {
    1: 'Miguel',
    2: 'Ángel',
    3: 'Max',
    4: 'Diego'
}

# Errores propios solo heredan de Exception
class FaltaMoneyError(Exception):
    pass

# try:
#     print(diccionario[10])
# except KeyError:
#     print("Esa llave no existe.")
# PASAN COSITAS...
raise FaltaMoneyError('Te falta money, chavo.')