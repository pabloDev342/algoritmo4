# ============================================================
# EXAMEN A - ESTRUCTURAS DE DATOS
# HISTORIAL DE NAVEGACIÓN
# ============================================================


# ============================================================
# PUNTO 1: CLASE NODO
# ============================================================

class Nodo:

    def __init__(self, url, titulo, tiempo):

        # Datos que guarda cada página
        self.url = url
        self.titulo = titulo
        self.tiempo = tiempo

        # Apunta al siguiente nodo
        self.siguiente = None


# ============================================================
# PUNTO 1: CLASE HISTORIAL
# ============================================================

class Historial:

    def __init__(self):

        # Guarda el primer nodo de la lista
        # None significa que la lista está vacía
        self.inicio = None


    # ========================================================
    # PUNTO 2: VISITAR / AGREGAR PÁGINA
    # ========================================================

    def visitar(self, url, titulo, tiempo):

        # Creamos un nuevo nodo
        nuevo = Nodo(url, titulo, tiempo)

        # El nuevo nodo apunta al que estaba de primero
        nuevo.siguiente = self.inicio

        # Ahora el nuevo nodo es el primero
        self.inicio = nuevo


    # ========================================================
    # PUNTO 3: TIEMPO TOTAL - RECURSIVO
    # ========================================================

    def tiempo_total(self):

        # Comenzamos la recursividad desde el inicio
        return self._tiempo_total(self.inicio)


    def _tiempo_total(self, nodo):

        # CASO BASE:
        # Si no hay nodo, llegamos al final
        if nodo is None:
            return 0

        # Sumamos el tiempo actual
        # y seguimos con el siguiente nodo
        return nodo.tiempo + self._tiempo_total(nodo.siguiente)


    # ========================================================
    # PUNTO 4: BUSCAR POR DOMINIO - RECURSIVO
    # ========================================================

    def buscar_por_dominio(self, texto):

        # Creamos una nueva lista
        # para NO modificar la lista original
        nueva = Historial()

        # Buscamos recursivamente
        self._buscar(self.inicio, texto, nueva)

        # Retornamos la nueva lista
        return nueva


    def _buscar(self, nodo, texto, nueva):

        # CASO BASE:
        # Llegamos al final de la lista
        if nodo is None:
            return

        # Revisamos si el texto está dentro de la URL
        if texto in nodo.url:

            # Si coincide, copiamos la página
            nueva.visitar(
                nodo.url,
                nodo.titulo,
                nodo.tiempo
            )

        # Pasamos al siguiente nodo
        self._buscar(nodo.siguiente, texto, nueva)


    # ========================================================
    # PUNTO 5: ELIMINAR PÁGINAS RÁPIDAS - RECURSIVO
    # ========================================================

    def eliminar_rapidas(self, segundos):

        # La función recursiva devuelve
        # cuál debe ser el nuevo inicio
        self.inicio = self._eliminar(
            self.inicio,
            segundos
        )


    def _eliminar(self, nodo, segundos):

        # CASO BASE:
        # Si no existe nodo, terminamos
        if nodo is None:
            return None

        # Primero revisamos el resto de la lista
        nodo.siguiente = self._eliminar(
            nodo.siguiente,
            segundos
        )

        # Si estuvo menos tiempo del permitido
        # eliminamos este nodo
        if nodo.tiempo < segundos:

            # Saltamos el nodo actual
            return nodo.siguiente

        # Si tiene suficiente tiempo,
        # conservamos el nodo
        return nodo


    # ========================================================
    # MÉTODO MOSTRAR
    # ========================================================

    def mostrar(self):

        # Comenzamos desde el inicio
        actual = self.inicio

        # Recorremos todos los nodos
        while actual is not None:

            print(
                "URL:", actual.url,
                "| Título:", actual.titulo,
                "| Tiempo:", actual.tiempo,
                "segundos"
            )

            # Pasamos al siguiente
            actual = actual.siguiente


# ============================================================
# PRUEBAS
# ============================================================

if __name__ == "__main__":

    # Creamos el historial
    historial = Historial()


    # Agregamos páginas
    historial.visitar(
        "https://www.google.com/search",
        "Búsqueda Google",
        15
    )

    historial.visitar(
        "https://www.youtube.com/watch",
        "Video YouTube",
        300
    )

    historial.visitar(
        "https://www.github.com/repo",
        "GitHub Repo",
        180
    )

    historial.visitar(
        "https://www.youtube.com/home",
        "YouTube Home",
        45
    )

    historial.visitar(
        "https://www.google.com/maps",
        "Google Maps",
        5
    )


    # ========================================================
    # MOSTRAR HISTORIAL
    # ========================================================

    print("\nHISTORIAL INICIAL:")

    historial.mostrar()


    # ========================================================
    # TIEMPO TOTAL
    # ========================================================

    print("\nTIEMPO TOTAL:")

    print(historial.tiempo_total(), "segundos")


    # ========================================================
    # BUSCAR YOUTUBE
    # ========================================================

    print("\nPÁGINAS DE YOUTUBE:")

    youtube = historial.buscar_por_dominio("youtube")

    youtube.mostrar()


    # ========================================================
    # ELIMINAR PÁGINAS DE MENOS DE 30 SEGUNDOS
    # ========================================================

    print("\nELIMINANDO PÁGINAS DE MENOS DE 30 SEGUNDOS:")

    historial.eliminar_rapidas(30)

    historial.mostrar()