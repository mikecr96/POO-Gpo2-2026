class AlbumPanini:
    num_max = 600
    def __init__(self, propietario:str, tipo:str) -> None:
        self.propietario = propietario
        self.tipo = tipo
        self.estampas_pegadas = []

    def pegar_estampa(self, estampa):
        if len(self.estampas_pegadas) < AlbumPanini.num_max:
            for i in self.estampas_pegadas:
                if estampa.nombre == i.nombre and estampa.pais == i.pais:
                    if estampa.es_dorada == i.es_dorada:
                        print("Usted ya tiene esta estampa.")
                    elif estampa.es_dorada and not i.es_dorada:
                        indice = self.estampas_pegadas.index(i)
                        self.estampas_pegadas[indice] = estampa
                    else:
                        self.estampas_pegadas.append(estampa)
        else:
            print("Ya llenaste el álbum, seguramente eres rico.")

        """
        1. no puede haber jugadores repetidos
        2. privilegiamos doradas: si hay una no dorada la reemplazamos
        3. crear una variable que contenga los nombres de las estampas ya pegadas (list comprehension)       
        """