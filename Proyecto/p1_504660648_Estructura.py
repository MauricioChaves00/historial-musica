class NodoCancion:
    def __init__(self, titulo, artista):
        self.titulo = titulo
        self.artista = artista
        self.anterior = None
        self.siguiente = None


class HistorialMusical:
    def __init__(self):
        self.primera = None
        self.ultima = None
        self.actual = None

    def agregar_cancion(self, titulo, artista):
        titulo = titulo.strip()
        artista = artista.strip()

        if not titulo or not artista:
            raise ValueError("El título y el artista son obligatorios.")

        nueva = NodoCancion(titulo, artista)

        if self.primera is None:
            self.primera = nueva
            self.ultima = nueva
            self.actual = nueva
        else:
            nueva.anterior = self.ultima
            self.ultima.siguiente = nueva
            self.ultima = nueva

        return nueva

    def avanzar(self):
        if self.actual is None or self.actual.siguiente is None:
            return False

        self.actual = self.actual.siguiente
        return True

    def retroceder(self):
        if self.actual is None or self.actual.anterior is None:
            return False

        self.actual = self.actual.anterior
        return True

    def recorrer(self):
        nodo = self.primera

        while nodo is not None:
            yield nodo
            nodo = nodo.siguiente

    def buscar_cancion(self, titulo):
        titulo_buscado = titulo.strip().casefold()

        for nodo in self.recorrer():
            if nodo.titulo.casefold() == titulo_buscado:
                return nodo

        return None

    def eliminar_cancion(self, titulo):
        nodo = self.buscar_cancion(titulo)

        if nodo is None:
            return False

        anterior = nodo.anterior
        siguiente = nodo.siguiente

        # Reconectar el lado anterior o actualizar el inicio.
        if anterior is None:
            self.primera = siguiente
        else:
            anterior.siguiente = siguiente

        # Reconectar el lado siguiente o actualizar el final.
        if siguiente is None:
            self.ultima = anterior
        else:
            siguiente.anterior = anterior

        # Si eliminamos la actual, preferimos la siguiente.
        if self.actual is nodo:
            if siguiente is not None:
                self.actual = siguiente
            else:
                self.actual = anterior

        # Separar el nodo eliminado del historial.
        nodo.anterior = None
        nodo.siguiente = None

        return True