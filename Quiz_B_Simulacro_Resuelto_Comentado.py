"""
SIMULACRO DE QUIZ B - ALGORITMOS DE ORDENAMIENTO
SOLUCIÓN RESUELTA Y COMENTADA
================================================

Este archivo contiene:
- La respuesta razonada de cada caso.
- Complejidad temporal y espacial.
- Estabilidad.
- Por qué los otros algoritmos no son la mejor elección.
- Implementaciones completas y pruebas.

Algoritmos estudiados:
Burbuja, Inserción, Quick Sort, Counting Sort, Bucket Sort,
Radix Sort, Heap Sort y Merge Sort.

NOTA SOBRE ESPACIO:
Cuando un enunciado pide no modificar la lista original, la solución crea
una copia. Esa copia ocupa O(n). La complejidad auxiliar del algoritmo
puede ser menor, pero el espacio total incluye la copia de salida.
"""

# ================================================================
# CASO 1. REGISTRO DE ESTUDIANTES EN UNA PLATAFORMA
# ================================================================
"""
PROBLEMA:
Hay aproximadamente 300 estudiantes. Sus notas son decimales entre 0.0
y 5.0. La lista está casi ordenada. Se ordena ascendentemente y se debe
conservar el orden original cuando dos estudiantes tienen la misma nota.

ALGORITMO ELEGIDO: INSERTION SORT (ORDENAMIENTO POR INSERCIÓN).

JUSTIFICACIÓN:
Insertion Sort es adecuado para listas pequeñas o casi ordenadas.
Va tomando cada elemento y lo inserta en la posición correcta de la parte
que ya está ordenada. Si la lista está casi ordenada, realiza pocos
desplazamientos.

COMPLEJIDAD:
- Mejor caso: O(n), cuando ya está ordenada.
- Caso promedio: O(n²).
- Peor caso: O(n²), cuando está ordenada al revés.
- Espacio auxiliar: O(1) si se ordena directamente.
- En esta solución se copia la lista para no modificar la original:
  espacio total O(n), más O(1) auxiliar.

ESTABILIDAD:
Es estable si solo desplazamos elementos cuando la nota anterior es
MAYOR (>) que la nota actual. Si las notas son iguales, no se intercambian,
por lo que mantienen su orden de entrada.

¿POR QUÉ NO LOS DEMÁS?
- Burbuja: también puede aprovechar que la lista está casi ordenada,
  pero normalmente hace más comparaciones/intercambios y no aporta ventaja.
- Quick Sort: promedio O(n log n), pero es menos atractivo para solo 300
  elementos casi ordenados; una implementación simple puede degradarse
  a O(n²), y no es estable normalmente.
- Counting Sort: las notas son decimales; no se puede usar directamente
  como índices de un arreglo de conteo.
- Bucket Sort: podría funcionar con notas normalizadas, pero exige
  distribuir los datos en cubetas y aquí Insertion Sort es más simple.
- Radix Sort: no es directo para notas decimales y no hace falta.
- Heap Sort: O(n log n), pero no es estable y no aprovecha que casi
  todos los elementos ya estén ordenados.
- Merge Sort: estable y O(n log n), pero usa memoria auxiliar O(n);
  para una lista pequeña y casi ordenada, Inserción puede ser más simple.
"""

def resolver_caso_1(estudiantes):
    """Devuelve una copia ordenada por nota ascendente; es estable."""
    resultado = estudiantes.copy()

    for i in range(1, len(resultado)):
        actual = resultado[i]
        j = i - 1

        # Usar > y no >= conserva el orden de las notas iguales.
        while j >= 0 and resultado[j][1] > actual[1]:
            resultado[j + 1] = resultado[j]
            j -= 1

        resultado[j + 1] = actual

    return resultado


# ================================================================
# CASO 2. CLASIFICACIÓN DE PRODUCTOS POR EXISTENCIAS
# ================================================================
"""
PROBLEMA:
Hay 500.000 productos. La cantidad disponible es un entero entre 0 y 100.
Se requiere ordenar ascendentemente por cantidad, sin modificar la lista.

ALGORITMO ELEGIDO: COUNTING SORT (ORDENAMIENTO POR CONTEO) ESTABLE.

JUSTIFICACIÓN:
Counting Sort es ideal cuando las claves son enteros y su rango es pequeño.
En vez de comparar todos los productos entre sí, cuenta cuántas veces
aparece cada cantidad y calcula las posiciones de salida.

Como cada producto contiene más información que la cantidad, se utiliza
una versión estable que coloca los registros completos en el resultado.

COMPLEJIDAD:
- Tiempo: O(n + k), donde n es el número de productos y k=101 valores
  posibles (0 a 100).
- Espacio: O(n + k), por el arreglo de salida y los conteos.
- Como k es pequeño y fijo, el tiempo es prácticamente O(n).

ESTABILIDAD:
Sí, esta implementación es estable. Al recorrer la entrada de derecha
a izquierda al construir la salida, los productos con la misma cantidad
conservan su orden relativo original.

¿POR QUÉ NO LOS DEMÁS?
- Burbuja e Inserción: O(n²) en promedio/peor caso; demasiado lentos
  para 500.000 registros.
- Quick Sort: promedio O(n log n), pero compara elementos aunque el rango
  de claves sea diminuto; además, normalmente no es estable.
- Bucket Sort: posible, pero Counting Sort aprovecha directamente que
  hay solo 101 valores enteros posibles.
- Radix Sort: puede ordenar enteros, pero requiere procesar dígitos;
  Counting Sort es más directo para este rango tan pequeño.
- Heap Sort: O(n log n), pero no es estable y hace comparaciones
  innecesarias frente al rango pequeño.
- Merge Sort: estable y O(n log n), pero Counting Sort puede ser lineal
  porque el rango k es muy pequeño.
"""

def resolver_caso_2(inventario):
    """Counting Sort estable para cantidades enteras entre 0 y 100."""
    minimo = 0
    maximo = 100
    k = maximo - minimo + 1

    conteos = [0] * k

    # Contar la frecuencia de cada cantidad.
    for producto in inventario:
        cantidad = producto[1]
        if cantidad < minimo or cantidad > maximo:
            raise ValueError("La cantidad debe estar entre 0 y 100.")
        conteos[cantidad - minimo] += 1

    # Convertir frecuencias en posiciones acumuladas.
    for i in range(1, k):
        conteos[i] += conteos[i - 1]

    resultado = [None] * len(inventario)

    # Recorrer de derecha a izquierda para mantener estabilidad.
    for producto in reversed(inventario):
        cantidad = producto[1]
        indice = cantidad - minimo
        posicion = conteos[indice] - 1
        resultado[posicion] = producto
        conteos[indice] -= 1

    return resultado


# ================================================================
# CASO 3. PAQUETES POR CÓDIGO DE IDENTIFICACIÓN
# ================================================================
"""
PROBLEMA:
Hay 5 millones de paquetes con códigos enteros no negativos de exactamente
10 dígitos. El rango es enorme y se requiere orden ascendente.

ALGORITMO ELEGIDO: RADIX SORT LSD EN BASE 10.

JUSTIFICACIÓN:
Counting Sort directo necesitaría un arreglo proporcional al rango de
códigos, que puede acercarse a 10.000 millones de posiciones. Sería
desperdiciar memoria.

Radix Sort ordena por un dígito a la vez: unidades, decenas, centenas,
etc. Cada pasada usa un Counting Sort estable sobre el dígito actual.
Como todos los códigos tienen 10 dígitos, se hacen 10 pasadas.

COMPLEJIDAD:
- O(d(n+b)), donde d=10 dígitos y b=10 valores posibles por dígito.
- Con d y b constantes, el tiempo es O(n).
- Espacio: O(n+b), por la lista auxiliar y el conteo de 10 dígitos.

ESTABILIDAD:
Radix Sort LSD necesita que cada pasada sea estable. Así, al ordenar
un dígito más significativo, no se pierde el orden que ya se consiguió
con los dígitos menos significativos.

¿POR QUÉ NO LOS DEMÁS?
- Burbuja e Inserción: O(n²), inviables para millones de registros.
- Quick Sort: promedio O(n log n), pero no aprovecha que los códigos
  tienen una cantidad fija de dígitos.
- Counting Sort directo: el rango de códigos es demasiado grande.
- Bucket Sort: no se garantiza una distribución uniforme que permita
  repartir los códigos de manera eficiente.
- Heap Sort: O(n log n), pero Radix puede acercarse a O(n) con 10 dígitos.
- Merge Sort: O(n log n), estable, pero requiere más trabajo de
  comparación que Radix para claves de longitud fija.
"""

def counting_sort_por_digito(paquetes, exponente):
    """Pasada estable de Counting Sort según un dígito decimal."""
    conteos = [0] * 10
    resultado = [None] * len(paquetes)

    # Contar el dígito que corresponde al exponente.
    for paquete in paquetes:
        digito = (paquete[1] // exponente) % 10
        conteos[digito] += 1

    # Calcular posiciones acumuladas.
    for i in range(1, 10):
        conteos[i] += conteos[i - 1]

    # Construir de derecha a izquierda para mantener estabilidad.
    for paquete in reversed(paquetes):
        digito = (paquete[1] // exponente) % 10
        posicion = conteos[digito] - 1
        resultado[posicion] = paquete
        conteos[digito] -= 1

    return resultado


def resolver_caso_3(paquetes):
    """Radix Sort LSD estable para códigos enteros no negativos de 10 dígitos."""
    resultado = paquetes.copy()

    if any(codigo < 0 or codigo > 9_999_999_999
           for _, codigo in resultado):
        raise ValueError("Los códigos deben ser enteros de hasta 10 dígitos.")

    exponente = 1

    # Diez pasadas: unidades hasta miles de millones.
    for _ in range(10):
        resultado = counting_sort_por_digito(resultado, exponente)
        exponente *= 10

    return resultado


# ================================================================
# CASO 4. CLASIFICACIÓN DE RESULTADOS DE UNA COMPETENCIA
# ================================================================
"""
PROBLEMA:
Hay 2 millones de participantes con puntajes enteros de rango amplio.
Se requiere orden descendente. No importa conservar el orden original
de participantes con el mismo puntaje y la memoria es limitada.

ALGORITMO ELEGIDO: HEAP SORT.

JUSTIFICACIÓN:
Heap Sort tiene O(n log n) en mejor, promedio y peor caso. Su versión
in-place usa O(1) espacio auxiliar y no necesita una lista auxiliar
completa. Para obtener orden descendente, esta implementación construye
un min-heap y va colocando el menor elemento al final del arreglo.

La función copia primero la entrada para no modificar la lista original.
Por eso, el espacio total de esta función es O(n) por la copia; el
algoritmo Heap Sort en sí utiliza O(1) espacio auxiliar.

COMPLEJIDAD:
- Mejor caso: O(n log n).
- Caso promedio: O(n log n).
- Peor caso: O(n log n).
- Espacio auxiliar de Heap Sort: O(1).
- Espacio total aquí: O(n) por la copia que preserva la entrada.

ESTABILIDAD:
Heap Sort no es estable. En este caso no importa porque el enunciado
dice que no se necesita conservar el orden original cuando hay empates.

¿POR QUÉ NO LOS DEMÁS?
- Burbuja e Inserción: O(n²), demasiado lentos para 2 millones.
- Quick Sort: promedio O(n log n), pero puede llegar a O(n²) en el peor
  caso y su implementación habitual no garantiza el peor caso.
- Counting Sort: el rango de puntajes es amplio; el arreglo de conteo
  podría consumir demasiada memoria.
- Bucket Sort: requiere una distribución adecuada de los datos y cubetas
  bien dimensionadas; el enunciado no garantiza esa distribución.
- Radix Sort: podría ser una alternativa si se conoce el formato/rango
  de los enteros, pero no se especifica una cantidad fija de dígitos
  que permita justificarlo mejor que Heap Sort.
- Merge Sort: O(n log n), pero necesita O(n) memoria auxiliar.
"""

def heapify_min(arreglo, n, raiz):
    """Restaura la propiedad de min-heap desde la posición raiz."""
    menor = raiz
    izquierda = 2 * raiz + 1
    derecha = 2 * raiz + 2

    if izquierda < n and arreglo[izquierda][1] < arreglo[menor][1]:
        menor = izquierda

    if derecha < n and arreglo[derecha][1] < arreglo[menor][1]:
        menor = derecha

    if menor != raiz:
        arreglo[raiz], arreglo[menor] = arreglo[menor], arreglo[raiz]
        heapify_min(arreglo, n, menor)


def resolver_caso_4(participantes):
    """Heap Sort descendente; devuelve copia y no es estable."""
    resultado = participantes.copy()
    n = len(resultado)

    # Construir un min-heap.
    for i in range(n // 2 - 1, -1, -1):
        heapify_min(resultado, n, i)

    # Mover el mínimo al final en cada iteración.
    # Al terminar, el arreglo queda en orden descendente.
    for fin in range(n - 1, 0, -1):
        resultado[0], resultado[fin] = resultado[fin], resultado[0]
        heapify_min(resultado, fin, 0)

    return resultado


# ================================================================
# PRUEBAS DE LOS CUATRO CASOS
# ================================================================

if __name__ == "__main__":
    estudiantes = [
        ("E01", 3.8),
        ("E02", 2.5),
        ("E03", 4.2),
        ("E04", 2.5),
        ("E05", 3.9),
        ("E06", 1.8)
    ]
    copia_estudiantes = estudiantes.copy()
    orden_estudiantes = resolver_caso_1(estudiantes)
    print("CASO 1 - Estudiantes:")
    print(orden_estudiantes)
    assert [x[1] for x in orden_estudiantes] == sorted(x[1] for x in estudiantes)
    assert orden_estudiantes.index(("E02", 2.5)) < orden_estudiantes.index(("E04", 2.5))
    assert estudiantes == copia_estudiantes

    inventario = [
        ("P101", 12),
        ("P102", 3),
        ("P103", 12),
        ("P104", 0),
        ("P105", 7),
        ("P106", 3)
    ]
    copia_inventario = inventario.copy()
    orden_inventario = resolver_caso_2(inventario)
    print("\\nCASO 2 - Inventario:")
    print(orden_inventario)
    assert [x[1] for x in orden_inventario] == sorted(x[1] for x in inventario)
    assert inventario == copia_inventario
    # Estabilidad: P102 estaba antes que P106 y ambos tienen cantidad 3.
    assert orden_inventario.index(("P102", 3)) < orden_inventario.index(("P106", 3))

    paquetes = [
        ("PAQ01", 3819201745),
        ("PAQ02", 1023456789),
        ("PAQ03", 3819201701),
        ("PAQ04", 9999999999),
        ("PAQ05", 1023456700)
    ]
    copia_paquetes = paquetes.copy()
    orden_paquetes = resolver_caso_3(paquetes)
    print("\\nCASO 3 - Paquetes:")
    print(orden_paquetes)
    assert [x[1] for x in orden_paquetes] == sorted(x[1] for x in paquetes)
    assert paquetes == copia_paquetes

    participantes = [
        ("Ana", 850),
        ("Luis", 1200),
        ("Marta", 850),
        ("Carlos", 430),
        ("Sofia", 1600)
    ]
    copia_participantes = participantes.copy()
    orden_participantes = resolver_caso_4(participantes)
    print("\\nCASO 4 - Competencia:")
    print(orden_participantes)
    assert [x[1] for x in orden_participantes] == sorted(
        (x[1] for x in participantes), reverse=True
    )
    assert participantes == copia_participantes

    print("\\nTodas las pruebas terminaron correctamente.")
