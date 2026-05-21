from album import AlbumPanini
from jugador import Estampa, abrir_sobre

album = AlbumPanini('Miguel', 'Pasta dura')
estampas = abrir_sobre()
for estampa in estampas:
    album.pegar_estampa(estampa)
for estampa in estampas:
    album.pegar_estampa(estampa)
