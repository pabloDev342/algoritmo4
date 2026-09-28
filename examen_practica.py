# ============================================================
# PARCIAL - CONJUNTOS
# Validador de Sudoku + Sistema de Permisos
# ============================================================


# ============================================================
# PARTE 1: VALIDADOR DE SUDOKU
# ============================================================

# Estos son los números que debe tener cada fila,
# cada columna y cada cuadro 3x3.
NUMEROS_VALIDOS = {1, 2, 3, 4, 5, 6, 7, 8, 9}


# Este es el tablero de Sudoku que nos entrega el profesor.
TABLERO = [
    [5, 3, 4, 6, 7, 8, 9, 1, 2],
    [6, 7, 2, 1, 9, 5, 3, 4, 8],
    [1, 9, 8, 3, 4, 2, 5, 6, 7],
    [8, 5, 9, 7, 6, 1, 4, 2, 3],
    [4, 2, 6, 8, 5, 3, 7, 9, 1],
    [7, 1, 3, 9, 2, 4, 8, 5, 6],
    [9, 6, 1, 5, 3, 7, 2, 8, 4],
    [2, 8, 7, 4, 1, 9, 6, 3, 5],
    [3, 4, 5, 2, 8, 6, 1, 7, 9]
]


# ============================================================
# PUNTO 1.1 - VALIDAR UNA FILA
# ============================================================

def validar_fila(tablero, num_fila):

    # Sacamos la fila que queremos revisar.
    # Por ejemplo, si num_fila = 0, obtenemos la primera fila.
    fila = tablero[num_fila]

    # Convertimos la fila en un conjunto.
    # Los conjuntos no permiten elementos repetidos.
    fila = set(fila)

    # Comparamos la fila con los números válidos {1...9}.
    # Si son iguales, devuelve True.
    # Si son diferentes, devuelve False.
    return fila == NUMEROS_VALIDOS


# ============================================================
# PUNTO 1.2 - VALIDAR UNA COLUMNA
# ============================================================

def validar_columna(tablero, num_columna):

    # Creamos un conjunto vacío.
    # Aquí vamos a guardar los números de la columna.
    columna = set()

    # Recorremos todas las filas del tablero.
    for fila in tablero:

        # Tomamos el número que está en la columna indicada.
        # Ejemplo: si num_columna = 0,
        # tomamos el primer número de cada fila.
        columna.add(fila[num_columna])

    # Comparamos la columna con los números válidos.
    # Si tiene exactamente 1-9, devuelve True.
    return columna == NUMEROS_VALIDOS


# ============================================================
# PUNTO 1.3 - VALIDAR UN SUBCUADRO 3x3
# ============================================================

def validar_subcuadro(tablero, fila_inicio, col_inicio):

    # Creamos un conjunto vacío.
    # Aquí guardaremos los 9 números del cuadro 3x3.
    numeros = set()

    # Recorremos las 3 filas del subcuadro.
    for i in range(fila_inicio, fila_inicio + 3):

        # Recorremos las 3 columnas del subcuadro.
        for j in range(col_inicio, col_inicio + 3):

            # Obtenemos el número que está en:
            # fila i y columna j.
            numeros.add(tablero[i][j])

    # Comprobamos que el subcuadro tenga exactamente
    # los números del 1 al 9.
    return numeros == NUMEROS_VALIDOS


# ============================================================
# PARTE 2 - SISTEMA DE PERMISOS CON LISTAS
# ============================================================


# ============================================================
# CLASE NODO
# ============================================================

class Nodo:

    def __init__(self, dato):

        # Guardamos el dato dentro del nodo.
        self.dato = dato

        # Al principio no apunta a ningún otro nodo.
        self.siguiente = None


# ============================================================
# CLASE CONJUNTO
# ============================================================

class Conjunto:

    def __init__(self, elementos=None):

        # cabeza representa el primer nodo de la lista.
        self.cabeza = None

        # Guardamos cuántos elementos tiene el conjunto.
        self.tamaño = 0

        # Si recibimos elementos, los agregamos.
        if elementos:

            for e in elementos:
                self.agregar(e)


    # --------------------------------------------------------
    # SABER SI EL CONJUNTO ESTÁ VACÍO
    # --------------------------------------------------------

    def esta_vacio(self):

        # Si cabeza es None, no hay ningún nodo.
        return self.cabeza is None


    # --------------------------------------------------------
    # BUSCAR SI UN ELEMENTO PERTENECE AL CONJUNTO
    # --------------------------------------------------------

    def pertenece(self, x):

        # Comenzamos desde el primer nodo.
        actual = self.cabeza

        # Mientras exista un nodo...
        while actual:

            # Revisamos si el dato del nodo es igual a x.
            if actual.dato == x:

                # Lo encontramos.
                return True

            # Pasamos al siguiente nodo.
            actual = actual.siguiente

        # Si llegamos aquí, no encontramos el elemento.
        return False


    # --------------------------------------------------------
    # AGREGAR UN ELEMENTO
    # --------------------------------------------------------

    def agregar(self, x):

        # Primero revisamos si ya existe.
        if self.pertenece(x):

            # No lo agregamos porque un conjunto
            # no debe tener elementos repetidos.
            return False

        # Creamos un nuevo nodo.
        nuevo = Nodo(x)

        # El nuevo nodo apunta al que era el primero.
        nuevo.siguiente = self.cabeza

        # Ahora el nuevo nodo se convierte en el primero.
        self.cabeza = nuevo

        # Aumentamos el tamaño.
        self.tamaño += 1

        return True


    # --------------------------------------------------------
    # MOSTRAR EL CONJUNTO
    # --------------------------------------------------------

    def __str__(self):

        # Lista temporal para mostrar los elementos.
        elementos = []

        # Comenzamos desde el primer nodo.
        actual = self.cabeza

        # Recorremos la lista.
        while actual:

            # Convertimos el dato a texto y lo guardamos.
            elementos.append(str(actual.dato))

            # Pasamos al siguiente nodo.
            actual = actual.siguiente

        # Formamos algo como:
        # {leer, escribir, eliminar}
        return "{" + ", ".join(elementos) + "}"


# ============================================================
# PUNTO 2.1 - VERIFICAR SI ES SUBCONJUNTO
# ============================================================

def es_subconjunto(conjunto_a, conjunto_b):

    # Empezamos desde el primer nodo del conjunto A.
    actual = conjunto_a.cabeza

    # Recorremos todos los elementos de A.
    while actual:

        # Preguntamos:
        # ¿El elemento actual de A está en B?
        if not conjunto_b.pertenece(actual.dato):

            # Si encontramos uno que NO está en B,
            # entonces A NO es subconjunto de B.
            return False

        # Pasamos al siguiente nodo de A.
        actual = actual.siguiente

    # Si llegamos hasta aquí,
    # significa que TODOS los elementos de A
    # estaban dentro de B.
    return True


# ============================================================
# PUNTO 2.2 - VERIFICAR PERMISOS DEL USUARIO
# ============================================================

def tiene_permisos(permisos_usuario, permisos_requeridos):

    # Para que el usuario pueda realizar una acción,
    # TODOS los permisos requeridos deben estar
    # dentro de los permisos del usuario.
    #
    # Por eso preguntamos:
    #
    # permisos_requeridos ⊆ permisos_usuario

    return es_subconjunto(permisos_requeridos, permisos_usuario)


# ============================================================
# CÓDIGO DE PRUEBA
# ============================================================

if __name__ == "__main__":

    print("=" * 60)
    print("PARTE 1: VALIDADOR DE SUDOKU")
    print("=" * 60)


    # --------------------------------------------------------
    # PROBAR FILAS
    # --------------------------------------------------------

    print("\n📋 Validando filas:")

    # Vamos a revisar las 9 filas.
    for i in range(9):

        # Llamamos a nuestra función.
        resultado = validar_fila(TABLERO, i)

        # Mostramos el resultado.
        print(f"  Fila {i+1}: {'✓' if resultado else '✗'}")


    # --------------------------------------------------------
    # PROBAR COLUMNAS
    # --------------------------------------------------------

    print("\n📋 Validando columnas:")

    # Vamos a revisar las 9 columnas.
    for j in range(9):

        resultado = validar_columna(TABLERO, j)

        print(f"  Columna {j+1}: {'✓' if resultado else '✗'}")


    # --------------------------------------------------------
    # PROBAR SUBCUADROS 3x3
    # --------------------------------------------------------

    print("\n📋 Validando subcuadros 3x3:")

    # Las posiciones iniciales pueden ser 0, 3 y 6.
    for fi in [0, 3, 6]:

        for ci in [0, 3, 6]:

            resultado = validar_subcuadro(TABLERO, fi, ci)

            print(f"  Subcuadro ({fi+1},{ci+1}): {'✓' if resultado else '✗'}")


    print("\n" + "=" * 60)
    print("PARTE 2: SISTEMA DE PERMISOS")
    print("=" * 60)


    # --------------------------------------------------------
    # CREAR ROLES
    # --------------------------------------------------------

    # El administrador tiene muchos permisos.
    admin = Conjunto([
        "leer",
        "escribir",
        "eliminar",
        "crear_usuarios"
    ])

    # El editor tiene dos permisos.
    editor = Conjunto([
        "leer",
        "escribir"
    ])

    # El viewer solamente puede leer.
    viewer = Conjunto([
        "leer"
    ])


    print("\n👤 Roles definidos:")

    print(f"  Admin: {admin}")
    print(f"  Editor: {editor}")
    print(f"  Viewer: {viewer}")


    # --------------------------------------------------------
    # PROBAR SUBCONJUNTOS
    # --------------------------------------------------------

    print("\n🔍 Verificando subconjuntos:")

    # Viewer tiene solamente "leer".
    # Editor tiene "leer" y "escribir".
    # Por eso Viewer está dentro de Editor.
    print(
        f"  ¿Viewer ⊆ Editor? "
        f"{es_subconjunto(viewer, editor)}"
    )


    # Editor tiene "leer" y "escribir".
    # Admin tiene esos dos permisos también.
    print(
        f"  ¿Editor ⊆ Admin? "
        f"{es_subconjunto(editor, admin)}"
    )


    # Admin tiene permisos que Editor no tiene.
    # Por eso Admin NO es subconjunto de Editor.
    print(
        f"  ¿Admin ⊆ Editor? "
        f"{es_subconjunto(admin, editor)}"
    )


    # --------------------------------------------------------
    # PROBAR PERMISOS
    # --------------------------------------------------------

    print("\n🔐 Verificando permisos:")


    # Para editar se necesitan estos dos permisos.
    accion_editar = Conjunto([
        "leer",
        "escribir"
    ])


    # Para realizar la acción administrativa
    # se necesitan estos dos permisos.
    accion_admin = Conjunto([
        "crear_usuarios",
        "eliminar"
    ])


    print(f"  Acción editar requiere: {accion_editar}")
    print(f"  Acción admin requiere: {accion_admin}")


    # Editor tiene leer y escribir.
    # Por eso puede editar.
    print(
        f"\n  ¿Editor puede editar? "
        f"{tiene_permisos(editor, accion_editar)}"
    )


    # Viewer solamente tiene leer.
    # Le falta escribir.
    # Por eso NO puede editar.
    print(
        f"  ¿Viewer puede editar? "
        f"{tiene_permisos(viewer, accion_editar)}"
    )


    # Admin tiene crear_usuarios y eliminar.
    # Por eso puede realizar la acción administrativa.
    print(
        f"  ¿Admin puede hacer acción admin? "
        f"{tiene_permisos(admin, accion_admin)}"
    )


    # Editor no tiene crear_usuarios ni eliminar.
    # Por eso no puede realizar la acción administrativa.
    print(
        f"  ¿Editor puede hacer acción admin? "
        f"{tiene_permisos(editor, accion_admin)}"
    )