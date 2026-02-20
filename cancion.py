# -*- coding: utf-8 -*-
# ============================================
# REPRODUCTOR DE CANCIONES - Python 2.7
# ============================================

# Clase Cancion
# Cada cancion tiene:
# - nombre
# - duracion (en segundos)
# - enlace a la siguiente cancion
# - enlace a la cancion anterior
# Esto permite moverse hacia adelante y hacia atras en la lista
class Cancion:
    def __init__(self, nombre, duracion):
        self.nombre = nombre
        self.duracion = duracion
        self.siguiente = None  # apunta a la siguiente cancion
        self.anterior = None   # apunta a la cancion anterior

    # Metodo para mostrar duracion en formato mm:ss
    def duracion_formato(self):
        minutos = self.duracion // 60
        segundos = self.duracion % 60
        return "{}:{:02d}".format(minutos, segundos)


# Clase Reproductor
# Gestiona la lista de canciones y la reproduccion
# Utiliza una lista doblemente enlazada
class Reproductor:
    def __init__(self):
        self.cabeza = None  # primera cancion
        self.cola = None    # ultima cancion
        self.actual = None  # cancion que se esta reproduciendo

    # Metodo para verificar si la lista esta vacia
    def esta_vacia(self):
        return self.cabeza is None  # True si no hay canciones

    # Inserta una cancion al inicio
    def insertar_inicio(self, nombre, duracion):
        nuevo = Cancion(nombre, duracion)
        if self.esta_vacia():  # si la lista estaba vacia
            self.cabeza = nuevo
            self.cola = nuevo
            self.actual = nuevo  # la primera cancion agregada es la actual
        else:
            # Conecta el nuevo nodo al inicio
            nuevo.siguiente = self.cabeza
            self.cabeza.anterior = nuevo
            self.cabeza = nuevo

    # Inserta una cancion al final
    def insertar_final(self, nombre, duracion):
        nuevo = Cancion(nombre, duracion)
        if self.esta_vacia():  # lista vacia
            self.cabeza = nuevo
            self.cola = nuevo
            self.actual = nuevo
        else:
            # Conecta el nuevo nodo al final
            self.cola.siguiente = nuevo
            nuevo.anterior = self.cola
            self.cola = nuevo
        print("Cancion agregada")

    # Muestra todas las canciones
    def mostrar_lista(self):
        if self.esta_vacia():
            print("Lista vacia")
            return
        actual = self.cabeza
        print("\nLista de canciones:")
        while actual:
            # Marca la cancion que se esta reproduciendo
            if actual == self.actual:
                print("{} ({}) <-- Reproduciendo".format(actual.nombre, actual.duracion_formato()))
            else:
                print("{} ({})".format(actual.nombre, actual.duracion_formato()))
            actual = actual.siguiente

    # Reproduce la cancion actual
    def reproducir(self):
        if self.actual:
            print("Reproduciendo: {} ({})".format(self.actual.nombre, self.actual.duracion_formato()))
        else:
            print("No hay canciones")

    # Avanza a la siguiente cancion
    def siguiente(self):
        if self.actual and self.actual.siguiente:  # si hay siguiente
            self.actual = self.actual.siguiente
            self.reproducir()
        else:
            print("No hay siguiente cancion")

    # Retrocede a la cancion anterior
    def anterior(self):
        if self.actual and self.actual.anterior:  # si hay anterior
            self.actual = self.actual.anterior
            self.reproducir()
        else:
            print("No hay cancion anterior")

    # Elimina una cancion por nombre
    def eliminar_cancion(self, nombre):
        actual = self.cabeza
        while actual:
            if actual.nombre == nombre:
                # Si es la primera cancion
                if actual.anterior is None:
                    self.cabeza = actual.siguiente
                    if self.cabeza:
                        self.cabeza.anterior = None
                else:
                    actual.anterior.siguiente = actual.siguiente
                # Si no es la ultima cancion
                if actual.siguiente:
                    actual.siguiente.anterior = actual.anterior
                # Ajusta la cancion actual si se elimino
                if self.actual == actual:
                    self.actual = actual.siguiente or actual.anterior
                print("Cancion eliminada")
                return
            actual = actual.siguiente
        print("Cancion no encontrada")


# Funcion menu
# Muestra las opciones al usuario
def menu():
    print("\nREPRODUCTOR DE CANCIONES")
    print("1. Agregar cancion")
    print("2. Mostrar lista")
    print("3. Reproducir cancion actual")
    print("4. Siguiente cancion")
    print("5. Cancion anterior")
    print("6. Eliminar cancion")
    print("7. Salir")


# Programa principal
reproductor = Reproductor()

while True:
    menu()
    opcion = raw_input("Elige una opcion: ")  # raw_input() en Python 2

    # ===== Logica del menu =====
    if opcion == "1":
        nombre = raw_input("Nombre de la cancion: ")
        duracion = int(raw_input("Duracion de la cancion (en segundos): "))
        reproductor.insertar_final(nombre, duracion)
    elif opcion == "2":
        reproductor.mostrar_lista()
    elif opcion == "3":
        reproductor.reproducir()
    elif opcion == "4":
        reproductor.siguiente()
    elif opcion == "5":
        reproductor.anterior()
    elif opcion == "6":
        nombre = raw_input("Nombre de la cancion a eliminar: ")
        reproductor.eliminar_cancion(nombre)
    elif opcion == "7":
        print("Saliendo del reproductor...")
        break
    else:
        print("Opcion invalida")