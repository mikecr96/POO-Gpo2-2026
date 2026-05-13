class Estampa:
    def __init__(self, nombre, pais, es_dorada=False) -> None:
        self.nombre = nombre
        self.pais = pais
        self.es_dorada = es_dorada

def abrir_sobre():
    return [
        Estampa('Lionel Messi', 'Argentina', True),
        Estampa('Cristiano Ronaldo', 'Portugal', True),
        Estampa('Guillermo Ochoa', 'México'),
        Estampa('Kylian Mbappé', 'Francia'),
        Estampa('Luca Modrick', 'Croacia')
    ]