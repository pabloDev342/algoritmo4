class Cancion:
    def __init__(self, titulo, artista, duracion_segundos):
        self.titulo = titulo
        self.artista = artista
        self.duracion_segundos = duracion_segundos
        self.siguiente = None
        self.anterior = None

class ListaReproduccion:
    def __init__(self):
        self.cabeza = None
        self.actual = None

    def agregar_cancion(self, titulo, artista, duracion_segundos):
        nueva = Cancion(titulo, artista, duracion_segundos)

        if self.cabeza is None:
            self.cabeza = nueva
            self.actual = nueva
        else:
            temp = self.cabeza
            while temp.siguiente:
                temp = temp.siguiente
            temp.siguiente = nueva
            nueva.anterior = temp

    def mostrar_lista(self):
        temp = self.cabeza
        while temp:
            print(f"{temp.titulo} - {temp.artista} ({temp.duracion_segundos}s)")
            temp = temp.siguiente
