# ==========================================
# CLASE NODO
# ==========================================

class Nodo:

    def __init__(self, nota):

        # Guardamos la nota
        self.nota = nota

        # Apunta al siguiente nodo
        self.siguiente = None


# ==========================================
# CLASE LISTA
# ==========================================

class Lista:

    def __init__(self):

        # Inicio de la lista
        self.inicio = None


    # ======================================
    # AGREGAR
    # ======================================

    def agregar(self, nota):

        # Crear un nodo nuevo
        nuevo = Nodo(nota)

        # El nuevo nodo apunta al primero
        nuevo.siguiente = self.inicio

        # El nuevo nodo se convierte en el primero
        self.inicio = nuevo


    # ======================================
    # MOSTRAR
    # ======================================

    def mostrar(self):

        # Empezamos desde el inicio
        actual = self.inicio

        # Recorremos la lista
        while actual is not None:

            print("Nota:", actual.nota)

            # Pasamos al siguiente
            actual = actual.siguiente


    # ======================================
    # SUMAR NOTAS - RECURSIVO
    # ======================================

    def sumar(self):

        # Empezamos desde el inicio
        return self._sumar(self.inicio)


    def _sumar(self, nodo):

        # CASO BASE
        # Si no existe nodo, terminamos
        if nodo is None:
            return 0

        # Sumamos la nota actual
        # y seguimos con el siguiente
        return nodo.nota + self._sumar(nodo.siguiente)


# ==========================================
# PROGRAMA PRINCIPAL
# ==========================================

lista = Lista()

# Agregamos las notas
lista.agregar(3.0)
lista.agregar(4.0)
lista.agregar(5.0)
lista.agregar(4.5)


# Mostrar las notas
print("NOTAS:")

lista.mostrar()


# Sumar las notas
print("\nSUMA DE LAS NOTAS:")

print(lista.sumar())