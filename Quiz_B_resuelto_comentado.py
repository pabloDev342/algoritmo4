"""
QUIZ B - ALGORITMOS DE ORDENAMIENTO
Solución completa con explicaciones y comentarios para estudiar.

En cada caso se incluye:
1. El algoritmo elegido y la razón de la elección.
2. La complejidad temporal y espacial.
3. La estabilidad y por qué importa en ese caso.
4. Por qué otros algoritmos no son la mejor opción.
5. La implementación solicitada en Python.

NOTA:
Las funciones devuelven listas nuevas. No modifican las listas recibidas.
"""

# =============================================================================
# CASO 1 (1.7): SISTEMA DE TRIAJE EN URGENCIAS
# =============================================================================
#
# DATOS DEL PROBLEMA:
# - Hay aproximadamente 80.000 pacientes.
# - La prioridad es un número entero entre 1 y 5.
# - Solo se incluyen pacientes cuyo estado sea "atendido".
# - La prioridad se ordena de menor a mayor: 1, 2, 3, 4, 5.
# - Si dos pacientes tienen la misma prioridad, llega primero quien ingresó
#   antes, según "hora_ingreso".
#
# 1. ALGORITMO ELEGIDO: COUNTING SORT (ORDENAMIENTO POR CONTEO).
#
# ¿Por qué?
# La prioridad solo tiene 5 valores posibles. Counting Sort es eficiente
# cuando la clave por la que ordenamos es un número entero de rango pequeño.
#
# Para garantizar la regla de llegada, aunque la lista no venga ordenada por
# hora, hacemos dos ordenamientos estables:
#   a) Primero ordenamos por hora de ingreso (0 a 1439 minutos del día).
#   b) Después ordenamos por prioridad (1 a 5).
#
# Como el segundo Counting Sort es estable, los pacientes con igual prioridad
# conservan el orden cronológico que se obtuvo en el primer paso.
#
# IMPORTANTE: el enunciado entrega la hora como "HH:MM", sin fecha. Por eso
# asumimos que los pacientes de un reporte pertenecen al mismo día/turno.
# Si se mezclaran varios días, el dato tendría que incluir también la fecha.
#
# 2. COMPLEJIDAD TEMPORAL:
# Sea n = 80.000 y k = 5 prioridades.
# - Filtrar pacientes: O(n).
# - Ordenar por hora: O(n + 1440), porque hay 1440 minutos posibles en un día.
# - Ordenar por prioridad: O(n + k).
# Total: O(3n + 1440 + k), que se expresa como O(n + 1440 + k).
# Como 1440 y k=5 son constantes pequeñas, el comportamiento es O(n).
#
# 3. COMPLEJIDAD ESPACIAL:
# O(n + 1440 + k), es decir O(n), por las listas auxiliares y el arreglo
# de conteo. Se necesita memoria adicional, pero el rango de las claves es
# pequeño.
#
# 4. ESTABILIDAD:
# Counting Sort se implementa de forma estable. Esto importa porque, después
# de ordenar por hora, el ordenamiento por prioridad debe conservar el orden
# de llegada entre pacientes con la misma prioridad.
#
# ¿POR QUÉ NO LOS OTROS ALGORITMOS?
# - Quick Sort: normalmente tiene O(n log n), pero puede llegar a O(n²) en
#   el peor caso y su versión común no es estable.
# - Heap Sort: tiene O(n log n), pero normalmente no es estable; además,
#   hace más trabajo que contar solo 5 prioridades.
# - Merge Sort: es estable y predecible, pero O(n log n) es más costoso que
#   Counting Sort cuando la clave solo tiene 5 valores.
# - Radix Sort: se usa más cuando las claves tienen varios dígitos; aquí la
#   prioridad tiene un rango muy pequeño, así que Counting Sort es más simple.
#
# IMPLEMENTACIÓN
# -----------------------------------------------------------------------------


def _counting_sort_estable(elementos, obtener_clave, valor_minimo, valor_maximo):
    """
    Ordena una lista por una clave entera usando Counting Sort estable.

    elementos:
        Lista que queremos ordenar.
    obtener_clave:
        Función que obtiene el número por el que se ordena cada elemento.
    valor_minimo y valor_maximo:
        Rango posible de las claves.

    ¿Qué significa estable?
    Si dos elementos tienen la misma clave, quedan en el mismo orden relativo
    en el que estaban antes de este ordenamiento.
    """

    # Si la lista está vacía, no hay nada que ordenar.
    if not elementos:
        return []

    # Creamos un contador para cada valor posible.
    # Por ejemplo, para prioridades 1..5 se crean 5 posiciones.
    cantidad_valores = valor_maximo - valor_minimo + 1
    conteo = [0] * cantidad_valores

    # PASO 1: contar cuántas veces aparece cada clave.
    for elemento in elementos:
        clave = obtener_clave(elemento)

        # Convertimos la clave a un índice que comienza en cero.
        indice = clave - valor_minimo

        if indice < 0 or indice >= cantidad_valores:
            raise ValueError("La clave está fuera del rango indicado.")

        conteo[indice] += 1

    # PASO 2: acumular los conteos.
    # Después de esto, cada posición indica cuántos elementos tienen una
    # clave menor o igual a esa posición.
    for i in range(1, cantidad_valores):
        conteo[i] += conteo[i - 1]

    # PASO 3: colocar los elementos en su posición final.
    resultado = [None] * len(elementos)

    # Se recorre de DERECHA a IZQUIERDA.
    # Este detalle es el que permite que Counting Sort sea estable.
    for i in range(len(elementos) - 1, -1, -1):
        elemento = elementos[i]
        clave = obtener_clave(elemento)
        indice = clave - valor_minimo

        conteo[indice] -= 1
        posicion_final = conteo[indice]
        resultado[posicion_final] = elemento

    return resultado


def _hora_a_minutos(hora):
    """
    Convierte una hora "HH:MM" a minutos desde las 00:00.

    Ejemplo:
        "08:14" = 8 * 60 + 14 = 494 minutos.
    """
    horas, minutos = hora.split(":")
    return int(horas) * 60 + int(minutos)


def ordenar_pacientes(pacientes):
    """
    Devuelve una NUEVA lista con los pacientes atendidos ordenados por:

    1. Prioridad ascendente: prioridad 1 aparece primero.
    2. Hora de ingreso ascendente: en una misma prioridad, llega primero
       quien ingresó antes.

    La lista original no se modifica.
    """

    # PASO 1: filtrar. Los pacientes que abandonaron no entran al reporte.
    atendidos = [
        paciente
        for paciente in pacientes
        if paciente["estado"] == "atendido"
    ]

    # PASO 2: ordenar cronológicamente por hora.
    # 00:00 equivale a 0 minutos y 23:59 equivale a 1439 minutos.
    pacientes_por_hora = _counting_sort_estable(
        atendidos,
        obtener_clave=lambda paciente: _hora_a_minutos(
            paciente["hora_ingreso"]
        ),
        valor_minimo=0,
        valor_maximo=1439
    )

    # PASO 3: ordenar por prioridad.
    # Como este ordenamiento es estable, los pacientes con la misma prioridad
    # conservan el orden por hora que acabamos de establecer.
    pacientes_por_prioridad = _counting_sort_estable(
        pacientes_por_hora,
        obtener_clave=lambda paciente: paciente["prioridad"],
        valor_minimo=1,
        valor_maximo=5
    )

    return pacientes_por_prioridad


# =============================================================================
# CASO 2 (1.7): RANKING DE PRODUCTOS EN E-COMMERCE
# =============================================================================
#
# DATOS DEL PROBLEMA:
# - Hay 2.000.000 de productos.
# - Cada producto es una tupla: (id_producto, rating, ventas_mes).
# - El rating es decimal, entre 0.0 y 5.0.
# - Se ordena de MAYOR a MENOR rating.
# - Si dos ratings son iguales, se conserva el orden original.
# - Hay memoria auxiliar suficiente y el proceso debe ser predecible.
#
# 1. ALGORITMO ELEGIDO: MERGE SORT (ORDENAMIENTO POR MEZCLA).
#
# ¿Por qué?
# Merge Sort siempre divide la lista en mitades y luego las mezcla ordenadas.
# Su tiempo es O(n log n) incluso en el peor caso. Por eso su rendimiento es
# predecible. Además, se puede implementar de forma estable.
#
# 2. COMPLEJIDAD TEMPORAL:
# - Peor caso: O(n log n).
# - Caso promedio: O(n log n).
# - Mejor caso: O(n log n) en esta implementación.
#
# 3. COMPLEJIDAD ESPACIAL:
# O(n) por la lista auxiliar usada para mezclar. La recursión utiliza además
# O(log n) espacio en la pila, que no cambia el orden total O(n).
#
# 4. ESTABILIDAD:
# Es estable. Cuando dos ratings son iguales, durante la mezcla se toma
# primero el elemento de la mitad izquierda. Así se conserva el orden original
# que ya venía priorizado por ventas_mes.
#
# ¿POR QUÉ NO LOS OTROS ALGORITMOS?
# - Quick Sort: su promedio es O(n log n), pero puede ser O(n²) en el peor
#   caso y normalmente no es estable. El enunciado pide un proceso predecible.
# - Heap Sort: tiene O(n log n), pero normalmente no es estable.
# - Counting Sort: el rating es decimal (float); no se puede usar directamente
#   como índice de un arreglo de conteo sin definir antes una escala discreta.
# - Radix Sort: no es la opción directa para estos ratings decimales; habría
#   que transformar y definir cuidadosamente su representación.
#
# IMPLEMENTACIÓN
# -----------------------------------------------------------------------------


def ordenar_productos(lista):
    """
    Recibe tuplas (id_producto, rating, ventas_mes) y devuelve una nueva lista
    ordenada por rating descendente, conservando el orden original en empates.

    Se usa Merge Sort con un único arreglo auxiliar para mantener el uso
    adicional de memoria en O(n).
    """

    # Copiamos la lista para no modificar la que recibió la función.
    resultado = list(lista)
    n = len(resultado)

    # Para una lista vacía o con un solo producto, ya está ordenada.
    if n <= 1:
        return resultado

    # Arreglo auxiliar que se reutiliza en todas las mezclas.
    auxiliar = [None] * n

    def merge_sort(inicio, fin):
        """
        Ordena el segmento desde 'inicio' (incluido) hasta 'fin' (excluido).
        """

        # Un segmento de cero o un elemento ya está ordenado.
        if fin - inicio <= 1:
            return

        # Encontramos el punto medio para dividir la lista.
        medio = (inicio + fin) // 2

        # Ordenamos la mitad izquierda.
        merge_sort(inicio, medio)

        # Ordenamos la mitad derecha.
        merge_sort(medio, fin)

        # MEZCLA: unir las dos mitades ordenadas.
        izquierda = inicio
        derecha = medio
        posicion = inicio

        while izquierda < medio and derecha < fin:

            rating_izquierdo = resultado[izquierda][1]
            rating_derecho = resultado[derecha][1]

            # Queremos rating descendente: el rating más alto va primero.
            #
            # Usamos >= y no >.
            # Si los ratings son iguales, elegimos el elemento izquierdo.
            # Esto conserva el orden original y hace estable a Merge Sort.
            if rating_izquierdo >= rating_derecho:
                auxiliar[posicion] = resultado[izquierda]
                izquierda += 1
            else:
                auxiliar[posicion] = resultado[derecha]
                derecha += 1

            posicion += 1

        # Si quedaron productos en la mitad izquierda, los copiamos.
        while izquierda < medio:
            auxiliar[posicion] = resultado[izquierda]
            izquierda += 1
            posicion += 1

        # Si quedaron productos en la mitad derecha, los copiamos.
        while derecha < fin:
            auxiliar[posicion] = resultado[derecha]
            derecha += 1
            posicion += 1

        # Pasamos el segmento ya mezclado desde el auxiliar al resultado.
        for i in range(inicio, fin):
            resultado[i] = auxiliar[i]

    # Ordenamos toda la lista, desde la posición 0 hasta n.
    merge_sort(0, n)

    return resultado


# =============================================================================
# CASO 3 (1.6): SISTEMA DE CÓDIGOS DE BARRAS EAN-13
# =============================================================================
#
# DATOS DEL PROBLEMA:
# - Hay 10.000.000 de códigos.
# - Cada código es un entero de exactamente 13 dígitos.
# - No se puede crear un arreglo de tamaño 10^13.
# - Se necesita un tiempo casi lineal.
#
# 1. ALGORITMO ELEGIDO: RADIX SORT.
#
# ¿Por qué?
# Radix Sort ordena los números dígito por dígito. Comienza por las unidades,
# sigue con las decenas, centenas y así hasta procesar los 13 dígitos.
# En cada pasada usa Counting Sort estable con base 10 (dígitos de 0 a 9).
# Por eso no necesita crear un arreglo gigantesco de tamaño 10^13.
#
# 2. COMPLEJIDAD TEMPORAL:
# O(d * (n + b)), donde:
#   n = 10.000.000 códigos
#   d = 13 dígitos
#   b = 10 valores posibles por dígito
#
# Sustituyendo:
# O(13 * (10.000.000 + 10)).
# Como d=13 y b=10 son constantes, el comportamiento es lineal respecto a n:
# O(n). Se realizan 13 pasadas sobre los códigos.
#
# 3. COMPLEJIDAD ESPACIAL:
# O(n + b): se necesita una lista auxiliar del tamaño de los datos y un arreglo
# de conteo de solo 10 posiciones. En este caso se expresa como O(n).
#
# 4. ESTABILIDAD:
# Cada pasada por dígito debe ser estable. Así, al ordenar el siguiente dígito,
# no se pierde el orden que ya se había conseguido con los dígitos anteriores.
#
# ¿POR QUÉ NO LOS OTROS ALGORITMOS?
# - Counting Sort directo: necesitaría un arreglo proporcional al rango de
#   códigos (cerca de 10^13 posiciones), lo que no cabe en memoria.
# - Merge Sort y Heap Sort: son O(n log n), no alcanzan el enfoque casi lineal
#   solicitado cuando los códigos tienen una cantidad fija de 13 dígitos.
# - Quick Sort: en promedio puede ser O(n log n), pero en el peor caso es
#   O(n²), por lo que no ofrece la misma garantía.
#
# IMPLEMENTACIÓN
# -----------------------------------------------------------------------------


def _counting_sort_por_digito(codigos, exponente):
    """
    Ordena establemente los códigos según un solo dígito.

    exponente = 1: unidades.
    exponente = 10: decenas.
    exponente = 100: centenas.

    La expresión (numero // exponente) % 10 obtiene el dígito que necesitamos.
    """

    n = len(codigos)

    # Arreglo donde guardaremos el resultado de esta pasada.
    salida = [0] * n

    # Base 10: diez posibles dígitos (0, 1, 2, ..., 9).
    conteo = [0] * 10

    # PASO 1: contar cuántas veces aparece cada dígito.
    for numero in codigos:
        digito = (numero // exponente) % 10
        conteo[digito] += 1

    # PASO 2: acumular los conteos para conocer las posiciones finales.
    for i in range(1, 10):
        conteo[i] += conteo[i - 1]

    # PASO 3: colocar los números en la salida.
    # Recorrer de derecha a izquierda hace estable esta pasada.
    for i in range(n - 1, -1, -1):
        numero = codigos[i]
        digito = (numero // exponente) % 10

        conteo[digito] -= 1
        posicion = conteo[digito]
        salida[posicion] = numero

    return salida


def ordenar_codigos(codigos):
    """
    Ordena los códigos EAN-13 de menor a mayor mediante Radix Sort.

    Devuelve una nueva lista y no modifica la lista original.
    El enunciado garantiza que los elementos son enteros de 13 dígitos.
    """

    # Hacemos una copia para no modificar la lista recibida.
    resultado = list(codigos)

    # Si no hay códigos, devolvemos la lista vacía.
    if not resultado:
        return resultado

    # Procesamos exactamente 13 posiciones: unidades hasta el dígito 13.
    exponente = 1

    for _ in range(13):
        # Ordenamos por el dígito de la posición actual.
        resultado = _counting_sort_por_digito(resultado, exponente)

        # Pasamos a la siguiente posición decimal.
        exponente *= 10

    return resultado


# =============================================================================
# CÓDIGO DE PRUEBA
# =============================================================================
#
# Este bloque se ejecuta cuando abrimos y ejecutamos este archivo directamente.
# Sirve para comprobar que las tres funciones producen los resultados esperados.
# =============================================================================

if __name__ == "__main__":

    print("=" * 60)
    print("PRUEBAS DEL QUIZ B DE ORDENAMIENTO")
    print("=" * 60)

    # -------------------------------------------------------------------------
    # PRUEBA CASO 1: TRIAJE
    # -------------------------------------------------------------------------
    print("\n--- CASO 1: Triaje en Urgencias ---")

    pacientes = [
        {"id_atencion": 1, "paciente": "Maria",  "prioridad": 3,
         "hora_ingreso": "08:00", "estado": "atendido"},
        {"id_atencion": 2, "paciente": "Carlos", "prioridad": 1,
         "hora_ingreso": "08:05", "estado": "atendido"},
        {"id_atencion": 3, "paciente": "Lucia",  "prioridad": 3,
         "hora_ingreso": "08:10", "estado": "atendido"},
        {"id_atencion": 4, "paciente": "Pablo",  "prioridad": 2,
         "hora_ingreso": "08:15", "estado": "abandono"},
        {"id_atencion": 5, "paciente": "Sofia",  "prioridad": 1,
         "hora_ingreso": "08:20", "estado": "atendido"},
        {"id_atencion": 6, "paciente": "Diego",  "prioridad": 5,
         "hora_ingreso": "08:25", "estado": "atendido"},
    ]

    resultado = ordenar_pacientes(pacientes)

    for p in resultado:
        print(
            f"  P{p['prioridad']} | {p['paciente']:7} | "
            f"id={p['id_atencion']} | {p['hora_ingreso']}"
        )

    # Prueba adicional: la lista puede llegar desordenada por hora.
    pacientes_desordenados = [
        {"id_atencion": 10, "paciente": "Ana", "prioridad": 2,
         "hora_ingreso": "09:30", "estado": "atendido"},
        {"id_atencion": 11, "paciente": "Luis", "prioridad": 2,
         "hora_ingreso": "09:10", "estado": "atendido"},
        {"id_atencion": 12, "paciente": "Eva", "prioridad": 1,
         "hora_ingreso": "09:20", "estado": "abandono"},
    ]

    resultado_desordenado = ordenar_pacientes(pacientes_desordenados)

    # Luis debe aparecer antes que Ana porque llegó a las 09:10.
    assert [p["paciente"] for p in resultado_desordenado] == ["Luis", "Ana"]

    # Comprobamos que no se modificó la lista original.
    assert len(pacientes) == 6

    # -------------------------------------------------------------------------
    # PRUEBA CASO 2: PRODUCTOS
    # -------------------------------------------------------------------------
    print("\n--- CASO 2: Ranking de productos ---")

    productos = [
        (101, 4.5, 320),
        (102, 3.8, 150),
        (103, 4.5, 410),
        (104, 5.0, 80),
        (105, 4.2, 600),
    ]

    resultado = ordenar_productos(productos)

    for p in resultado:
        print(f"  ID {p[0]} | rating={p[1]} | ventas={p[2]}")

    # Los productos 101 y 103 tienen el mismo rating.
    # Deben conservar su orden original: 101 antes que 103.
    assert [p[0] for p in resultado] == [104, 101, 103, 105, 102]

    # -------------------------------------------------------------------------
    # PRUEBA CASO 3: CÓDIGOS EAN-13
    # -------------------------------------------------------------------------
    print("\n--- CASO 3: Códigos EAN-13 ---")

    codigos = [
        7702011223344,
        7702011000111,
        7891234567890,
        7702011223344,
        4006381333931,
        7891234567890,
    ]

    resultado = ordenar_codigos(codigos)

    for codigo in resultado:
        print(f"  {codigo}")

    # Comprobamos que el resultado esté en orden ascendente.
    assert resultado == sorted(codigos)

    # Comprobamos que la lista original no haya sido modificada.
    assert codigos[0] == 7702011223344

    # También probamos que una lista vacía no produzca error.
    assert ordenar_codigos([]) == []

    print("\nTodas las pruebas terminaron correctamente.")
