"""
QUIZ B - ALGORITMOS DE ORDENAMIENTO
Versión corregida y comentada para estudiar.

En cada caso se explica:
1. Qué algoritmo se eligió.
2. Su complejidad temporal y espacial.
3. Por qué es importante que sea estable.
4. Cómo funciona el código paso a paso.
"""

# =============================================================================
# CASO 1: SISTEMA DE TRIAJE EN URGENCIAS
# =============================================================================
#
# Reglas:
# - Solo se incluyen pacientes con estado "atendido".
# - Primero van las prioridades más urgentes: 1, 2, 3, 4 y 5.
# - Si dos pacientes tienen la misma prioridad, va primero quien llegó antes.
#
# Algoritmo: COUNTING SORT (ordenamiento por conteo).
#
# ¿Por qué lo elegimos?
# La prioridad solo puede tomar 5 valores (del 1 al 5). Counting Sort es muy
# conveniente cuando la clave tiene un rango pequeño.
#
# Para cumplir también el orden de llegada, hacemos DOS ordenamientos estables:
# 1) Ordenamos por hora de ingreso (convertida a minutos desde las 00:00).
# 2) Ordenamos por prioridad.
#
# El segundo ordenamiento es estable, así que cuando dos pacientes tienen la
# misma prioridad conserva el orden por hora que conseguimos en el paso 1.
#
# Suposición: las horas pertenecen al mismo día/turno. Si los datos abarcan
# varios días, se debe usar fecha + hora como clave cronológica.
#
# Complejidad:
# - Tiempo: O(n + 1440 + n + 5) = O(n), porque 1440 y 5 son rangos fijos.
# - Espacio: O(n + 1440 + 5) = O(n).
# - Estabilidad: sí. Es necesaria para conservar el orden previo en los empates.


def counting_sort_estable(elementos, obtener_clave, valor_maximo):
    """
    Ordena elementos por una clave entera entre 0 y valor_maximo.

    Es estable: si dos elementos tienen la misma clave, conserva entre ellos
    el orden en el que aparecían en la lista original.

    Parámetros:
        elementos: lista de diccionarios u otros objetos.
        obtener_clave: función que obtiene la clave numérica de cada elemento.
        valor_maximo: valor máximo posible de la clave.
    """
    if not elementos:
        return []

    # 1. Crear el arreglo de conteo.
    # La posición 0 cuenta claves 0, la posición 1 cuenta claves 1, etc.
    conteo = [0] * (valor_maximo + 1)

    # 2. Contar cuántas veces aparece cada clave.
    for elemento in elementos:
        clave = obtener_clave(elemento)
        conteo[clave] += 1

    # 3. Acumular los conteos.
    # Así sabemos en qué posición final debe quedar cada clave.
    for i in range(1, len(conteo)):
        conteo[i] += conteo[i - 1]

    # 4. Colocar los elementos en el resultado.
    # Se recorre de DERECHA a IZQUIERDA para que el algoritmo sea estable.
    resultado = [None] * len(elementos)

    for i in range(len(elementos) - 1, -1, -1):
        elemento = elementos[i]
        clave = obtener_clave(elemento)

        conteo[clave] -= 1
        posicion = conteo[clave]
        resultado[posicion] = elemento

    return resultado


def hora_a_minutos(hora):
    """
    Convierte una hora en formato 'HH:MM' a minutos desde medianoche.

    Ejemplo: '08:14' -> 8 * 60 + 14 = 494.
    """
    horas, minutos = hora.split(":")
    return int(horas) * 60 + int(minutos)


def ordenar_pacientes(pacientes):
    """
    Filtra los pacientes atendidos y los ordena:
    primero por prioridad ascendente y, en caso de empate, por llegada.
    """
    # Paso 1: excluir a quienes abandonaron urgencias.
    atendidos = []
    for paciente in pacientes:
        if paciente["estado"] == "atendido":
            atendidos.append(paciente)

    # Paso 2: ordenar por hora de llegada.
    # Hay 24 * 60 = 1440 minutos posibles en un día.
    por_hora = counting_sort_estable(
        atendidos,
        obtener_clave=lambda paciente: hora_a_minutos(paciente["hora_ingreso"]),
        valor_maximo=1439
    )

    # Paso 3: ordenar por prioridad.
    # Como Counting Sort es estable, los empates de prioridad mantienen
    # el orden por hora que acabamos de establecer.
    por_prioridad = counting_sort_estable(
        por_hora,
        obtener_clave=lambda paciente: paciente["prioridad"],
        valor_maximo=5
    )

    return por_prioridad


# =============================================================================
# CASO 2: RANKING DE PRODUCTOS EN E-COMMERCE
# =============================================================================
#
# Cada producto es una tupla:
# (id_producto, rating, ventas_mes)
#
# Reglas:
# - Ordenar por rating de MAYOR a MENOR.
# - Si dos productos tienen el mismo rating, conservar el orden original.
#
# Algoritmo: MERGE SORT.
#
# ¿Por qué lo elegimos?
# Merge Sort tiene tiempo O(n log n) incluso en el peor caso, por lo que su
# comportamiento es predecible. Además, puede ser estable.
#
# Complejidad:
# - Tiempo: O(n log n) en mejor, promedio y peor caso.
# - Espacio auxiliar: O(n).
# - Estabilidad: sí, porque cuando los ratings son iguales elegimos primero
#   el elemento de la mitad izquierda.


def mezclar(arreglo, inicio, mitad, fin):
    """
    Combina dos mitades que ya están ordenadas por rating descendente.

    La mitad izquierda ocupa desde 'inicio' hasta 'mitad'.
    La mitad derecha ocupa desde 'mitad + 1' hasta 'fin'.
    """
    izquierda = arreglo[inicio:mitad + 1]
    derecha = arreglo[mitad + 1:fin + 1]

    i = 0  # posición actual en la mitad izquierda
    j = 0  # posición actual en la mitad derecha
    k = inicio  # posición donde escribiremos en el arreglo original

    # Comparar el primer elemento disponible de cada mitad.
    while i < len(izquierda) and j < len(derecha):

        # Usamos >= porque queremos rating descendente.
        # Si son iguales, gana el de la izquierda: esto conserva la estabilidad.
        if izquierda[i][1] >= derecha[j][1]:
            arreglo[k] = izquierda[i]
            i += 1
        else:
            arreglo[k] = derecha[j]
            j += 1

        k += 1

    # Copiar los elementos que hayan quedado en la mitad izquierda.
    while i < len(izquierda):
        arreglo[k] = izquierda[i]
        i += 1
        k += 1

    # Copiar los elementos que hayan quedado en la mitad derecha.
    while j < len(derecha):
        arreglo[k] = derecha[j]
        j += 1
        k += 1


def ordenar_merge(arreglo, inicio, fin):
    """
    Divide la lista en mitades, ordena cada mitad y luego las mezcla.
    """
    if inicio < fin:
        mitad = (inicio + fin) // 2

        # Ordenar recursivamente la mitad izquierda.
        ordenar_merge(arreglo, inicio, mitad)

        # Ordenar recursivamente la mitad derecha.
        ordenar_merge(arreglo, mitad + 1, fin)

        # Unir las dos mitades ya ordenadas.
        mezclar(arreglo, inicio, mitad, fin)


def ordenar_productos(lista):
    """
    Devuelve una copia de los productos ordenada por rating descendente.
    La lista original no se modifica.
    """
    copia = lista[:]

    # Si la lista está vacía, fin será -1 y la función recursiva no hará nada.
    ordenar_merge(copia, 0, len(copia) - 1)

    return copia


# =============================================================================
# CASO 3: CÓDIGOS DE BARRAS EAN-13
# =============================================================================
#
# Los códigos son enteros positivos de 13 dígitos.
#
# Algoritmo: RADIX SORT (por dígitos, de derecha a izquierda).
#
# ¿Por qué lo elegimos?
# Counting Sort necesitaría un arreglo para un rango gigantesco de posibles
# códigos. Radix Sort evita crear ese arreglo: ordena por cada dígito usando
# un Counting Sort estable con solo 10 posiciones (dígitos 0 a 9).
#
# Complejidad:
# - Tiempo: O(d * (n + b)), donde d es la cantidad de dígitos y b = 10.
# - Para EAN-13: O(13 * (n + 10)), que es lineal respecto a n.
# - Espacio: O(n + 10) = O(n).
# - Estabilidad: cada pasada por dígito es estable; esto permite que el orden
#   construido en las pasadas anteriores no se pierda.


def ordenar_por_posicion(arreglo, exponente):
    """
    Ordena establemente los números según un solo dígito.

    exponente = 1: unidades
    exponente = 10: decenas
    exponente = 100: centenas
    y así sucesivamente.
    """
    total = len(arreglo)
    resultado = [0] * total

    # Solo hay 10 dígitos posibles: del 0 al 9.
    conteo = [0] * 10

    # 1. Contar cuántas veces aparece cada dígito en esta posición.
    for numero in arreglo:
        digito = (numero // exponente) % 10
        conteo[digito] += 1

    # 2. Acumular para calcular las posiciones finales.
    for i in range(1, 10):
        conteo[i] += conteo[i - 1]

    # 3. Recorrer de derecha a izquierda para mantener la estabilidad.
    for i in range(total - 1, -1, -1):
        numero = arreglo[i]
        digito = (numero // exponente) % 10

        conteo[digito] -= 1
        resultado[conteo[digito]] = numero

    # 4. Copiar el resultado de esta pasada al arreglo original.
    for i in range(total):
        arreglo[i] = resultado[i]


def ordenar_codigos(codigos):
    """
    Ordena los códigos de menor a mayor usando Radix Sort.
    Devuelve una copia y no modifica la lista original.
    """
    copia = codigos[:]

    # Caso especial: max([]) produciría un error.
    if not copia:
        return copia

    # Radix Sort procesa primero unidades, luego decenas, centenas, etc.
    valor_maximo = max(copia)
    exponente = 1

    while valor_maximo // exponente > 0:
        ordenar_por_posicion(copia, exponente)
        exponente *= 10

    return copia


# =============================================================================
# PRUEBAS DE LOS TRES CASOS
# =============================================================================

if __name__ == "__main__":

    print("=" * 65)
    print("PRUEBAS DEL QUIZ B - ALGORITMOS DE ORDENAMIENTO")
    print("=" * 65)

    # -------------------------------------------------------------------------
    # PRUEBA CASO 1
    # La lista está intencionalmente mezclada por hora para comprobar que
    # el algoritmo sí ordena por llegada cuando hay prioridades repetidas.
    # -------------------------------------------------------------------------
    print("\nCASO 1: TRIAJE EN URGENCIAS")

    pacientes = [
        {"id_atencion": 1, "paciente": "Maria",  "prioridad": 3,
         "hora_ingreso": "08:10", "estado": "atendido"},
        {"id_atencion": 2, "paciente": "Carlos", "prioridad": 1,
         "hora_ingreso": "08:05", "estado": "atendido"},
        {"id_atencion": 3, "paciente": "Lucia",  "prioridad": 3,
         "hora_ingreso": "08:00", "estado": "atendido"},
        {"id_atencion": 4, "paciente": "Pablo",  "prioridad": 2,
         "hora_ingreso": "08:15", "estado": "abandono"},
        {"id_atencion": 5, "paciente": "Sofia",  "prioridad": 1,
         "hora_ingreso": "08:20", "estado": "atendido"},
        {"id_atencion": 6, "paciente": "Diego",  "prioridad": 5,
         "hora_ingreso": "08:25", "estado": "atendido"},
    ]

    resultado_pacientes = ordenar_pacientes(pacientes)

    for paciente in resultado_pacientes:
        print(
            f"Prioridad {paciente['prioridad']} | "
            f"{paciente['paciente']:7} | "
            f"Hora: {paciente['hora_ingreso']} | "
            f"Estado: {paciente['estado']}"
        )

    # -------------------------------------------------------------------------
    # PRUEBA CASO 2
    # Los productos 101 y 103 tienen rating 4.5. Deben quedar en ese mismo
    # orden porque 101 aparecía primero en la lista original.
    # -------------------------------------------------------------------------
    print("\nCASO 2: RANKING DE PRODUCTOS")

    productos = [
        (101, 4.5, 320),
        (102, 3.8, 150),
        (103, 4.5, 410),
        (104, 5.0, 80),
        (105, 4.2, 600),
    ]

    resultado_productos = ordenar_productos(productos)

    for producto in resultado_productos:
        print(
            f"ID: {producto[0]} | "
            f"Rating: {producto[1]} | "
            f"Ventas del mes: {producto[2]}"
        )

    # -------------------------------------------------------------------------
    # PRUEBA CASO 3
    # -------------------------------------------------------------------------
    print("\nCASO 3: CÓDIGOS EAN-13")

    codigos = [
        7702011223344,
        7702011000111,
        7891234567890,
        7702011223344,
        4006381333931,
        7891234567890,
    ]

    resultado_codigos = ordenar_codigos(codigos)

    for codigo in resultado_codigos:
        print(codigo)

    # Comprobaciones sencillas: si no hay error, las pruebas se cumplen.
    assert [p["paciente"] for p in resultado_pacientes] == [
        "Carlos", "Sofia", "Lucia", "Maria", "Diego"
    ]
    assert [p[0] for p in resultado_productos] == [
        104, 101, 103, 105, 102
    ]
    assert resultado_codigos == sorted(codigos)

    print("\nTodas las comprobaciones terminaron correctamente.")
