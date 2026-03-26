"""
═══════════════════════════════════════════════════════════════════════════════
📚 CONJUNTOS CON LISTAS ENLAZADAS
conjunto SIN usar set de Python,
sino usando una lista enlazada.
═══════════════════════════════════════════════════════════════════════════════
"""

# ═══════════════════════════════════════════════════════════════════════
# 🔹 NODO (estructura básica de la lista enlazada)
# ═══════════════════════════════════════════════════════════════════════

class Nodo:
    def __init__(self, dato):
        self.dato = dato          # Valor que guarda el nodo
        self.siguiente = None     # Apunta al siguiente nodo


# ═══════════════════════════════════════════════════════════════════════
# 🔹 CLASE CONJUNTO
# ═══════════════════════════════════════════════════════════════════════

class Conjunto:
    def __init__(self, elementos=None):
        self.cabeza = None   # Primer nodo de la lista
        self.tamaño = 0      # Cantidad de elementos
        
        # Si se envía una lista inicial, se agregan los elementos
        if elementos:
            for e in elementos:
                self.agregar(e)

    # ═══════════════════════════════════════════════════════════════════
    # 🔸 OPERACIONES BÁSICAS
    # ═══════════════════════════════════════════════════════════════════

    def esta_vacio(self):
        # Retorna True si no hay elementos
        return self.cabeza is None
    
    def cardinalidad(self):
        # Retorna cantidad de elementos
        return self.tamaño
    
    def pertenece(self, x):
        """Verifica si x está en el conjunto (x ∈ A)"""
        actual = self.cabeza
        
        # Recorre nodo por nodo
        while actual:
            if actual.dato == x:
                return True
            actual = actual.siguiente
        
        return False
    
    def agregar(self, x):
        """Agrega x si no existe (evita duplicados)"""
        
        # Si ya existe, no lo agrega
        if self.pertenece(x):
            return False
        
        # Crear nuevo nodo
        nuevo = Nodo(x)
        
        # Insertar al inicio (más eficiente)
        nuevo.siguiente = self.cabeza
        self.cabeza = nuevo
        
        self.tamaño += 1
        return True
    
    def eliminar(self, x):
        """Elimina un elemento del conjunto"""
        
        if self.esta_vacio():
            return False
        
        # Caso 1: el elemento está en la cabeza
        if self.cabeza.dato == x:
            self.cabeza = self.cabeza.siguiente
            self.tamaño -= 1
            return True
        
        # Caso 2: buscar en el resto
        actual = self.cabeza
        while actual.siguiente:
            if actual.siguiente.dato == x:
                actual.siguiente = actual.siguiente.siguiente
                self.tamaño -= 1
                return True
            actual = actual.siguiente
        
        return False
    
    def vaciar(self):
        """Elimina todos los elementos"""
        self.cabeza = None
        self.tamaño = 0


    # ═══════════════════════════════════════════════════════════════════
    # 🔸 OPERACIONES ENTRE CONJUNTOS
    # ═══════════════════════════════════════════════════════════════════

    def union(self, otro):
        """A ∪ B → todos los elementos sin repetir"""
        
        resultado = Conjunto()
        
        # Agregar elementos de A
        actual = self.cabeza
        while actual:
            resultado.agregar(actual.dato)
            actual = actual.siguiente
        
        # Agregar elementos de B
        actual = otro.cabeza
        while actual:
            resultado.agregar(actual.dato)
            actual = actual.siguiente
        
        return resultado
    
    def interseccion(self, otro):
        """A ∩ B → elementos en común"""
        
        resultado = Conjunto()
        actual = self.cabeza
        
        while actual:
            if otro.pertenece(actual.dato):
                resultado.agregar(actual.dato)
            actual = actual.siguiente
        
        return resultado
    
    def diferencia(self, otro):
        """A - B → elementos que están en A pero no en B"""
        
        resultado = Conjunto()
        actual = self.cabeza
        
        while actual:
            if not otro.pertenece(actual.dato):
                resultado.agregar(actual.dato)
            actual = actual.siguiente
        
        return resultado
    
    def diferencia_simetrica(self, otro):
        """A △ B → elementos que están en uno u otro pero no en ambos"""
        
        # Fórmula: (A - B) ∪ (B - A)
        return self.diferencia(otro).union(otro.diferencia(self))


    # ═══════════════════════════════════════════════════════════════════
    # 🔸 RELACIONES ENTRE CONJUNTOS
    # ═══════════════════════════════════════════════════════════════════

    def es_subconjunto(self, otro):
        """¿A ⊆ B? → todos los elementos de A están en B"""
        
        actual = self.cabeza
        while actual:
            if not otro.pertenece(actual.dato):
                return False
            actual = actual.siguiente
        
        return True
    
    def es_igual(self, otro):
        """¿A = B? → mismos elementos"""
        
        # Primero verifica tamaño
        if self.tamaño != otro.tamaño:
            return False
        
        # Luego verifica subconjunto
        return self.es_subconjunto(otro)


    # ═══════════════════════════════════════════════════════════════════
    # 🔸 UTILIDADES
    # ═══════════════════════════════════════════════════════════════════

    def copiar(self):
        """Crea una copia del conjunto"""
        
        copia = Conjunto()
        actual = self.cabeza
        
        while actual:
            copia.agregar(actual.dato)
            actual = actual.siguiente
        
        return copia
    
    def a_lista(self):
        """Convierte el conjunto a lista de Python"""
        
        resultado = []
        actual = self.cabeza
        
        while actual:
            resultado.append(actual.dato)
            actual = actual.siguiente
        
        return resultado

    def __str__(self):
        """Permite imprimir el conjunto bonito"""
        return "{" + ", ".join(str(x) for x in self.a_lista()) + "}"
    
    def __len__(self):
        """Permite usar len(A)"""
        return self.tamaño
    
    def __contains__(self, x):
        """Permite usar: x in A"""
        return self.pertenece(x)
    
    def __iter__(self):
        """Permite recorrer el conjunto con for"""
        
        actual = self.cabeza
        while actual:
            yield actual.dato
            actual = actual.siguiente


# ═══════════════════════════════════════════════════════════════════════
# 🔹 DEMO (PRUEBAS)
# ═══════════════════════════════════════════════════════════════════════

if __name__ == "__main__":
    
    # Crear conjuntos
    A = Conjunto([1, 2, 3, 4])
    B = Conjunto([3, 4, 5, 6])

    # Mostrar operaciones
    print(f"A = {A}")
    print(f"B = {B}")

    print(f"Unión: {A.union(B)}")
    print(f"Intersección: {A.interseccion(B)}")
    print(f"Diferencia A-B: {A.diferencia(B)}")
    print(f"Diferencia simétrica: {A.diferencia_simetrica(B)}")

    # Subconjuntos
    C = Conjunto([2, 3])
    print(f"C = {C}")
    print(f"C ⊆ A: {C.es_subconjunto(A)}")

    # Uso de operadores
    print(f"3 in A: {3 in A}")   # Usa __contains__
    print(f"len(A): {len(A)}")   # Usa __len__

    # Iterar
    print("Elementos de A:")
    for x in A:
        print(x)
