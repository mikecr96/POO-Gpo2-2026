class AlbumPanini:
    num_max = 600
    def __init__(self, propietario:str, tipo:str) -> None:
        self.propietario = propietario
        self.tipo = tipo
        self.estampas_pegadas = []

    def pegar_estampa(self, estampa):
        for c, pegada in enumerate(self.estampas_pegadas):
            if estampa.nombre == pegada.nombre and estampa.pais == pegada.pais:
                if estampa.es_dorada and not pegada.es_dorada:
                    print(f"Mejora! Estampa de {estampa.nombre} normal cambiada por dorada!")
                    self.estampas_pegadas[c] = estampa
                else:
                    print(f"Ya tienes a {estampa.nombre} en tu álbum.")
                    break
        else: # Nota: else en un for solo se ejectua si el ciclo terminó de forma natural (no hubo break)
            print(f"Estampa de {estampa.nombre} pegada a tu álbum")
            self.estampas_pegadas.append(estampa)