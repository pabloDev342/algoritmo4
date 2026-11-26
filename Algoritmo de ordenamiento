"""
═══════════════════════════════════════════════════════════════════════════════
                QUIZ B - ALGORITMOS DE ORDENAMIENTO
═══════════════════════════════════════════════════════════════════════════════

INSTRUCCIONES:
- En cada caso debes:
    1. ELEGIR el mejor algoritmo justificando complejidad temporal,
       espacial y estabilidad.
    2. EXPLICAR brevemente por qué los OTROS algoritmos no son los más
       adecuados.
    3. IMPLEMENTAR el algoritmo aplicado a la estructura de datos del caso.

═══════════════════════════════════════════════════════════════════════════════
"""

import time
import random


# ═══════════════════════════════════════════════════════════════════════════════
# CASO 1 (1.7): Sistema de Triaje en Urgencias
# ═══════════════════════════════════════════════════════════════════════════════

"""
CONTEXTO:
---------
Un hospital atiende ~80,000 pacientes al mes en urgencias. Cada paciente
recibe una PRIORIDAD entera del 1 al 5 al ingresar (1 = crítico, 5 = leve).
Al final de cada turno se genera un reporte ordenado por prioridad para
auditar la atención.

Cada registro tiene esta estructura:

    {
      "id_atencion": 33421,
      "paciente": "Maria Lopez",
      "prioridad": 2,                # entero 1..5
      "hora_ingreso": "08:14",       # cuándo LLEGÓ a urgencias
      "estado": "atendido"           # "atendido" | "abandono"
    }

REGLAS DEL REPORTE:
  R1) Solo entran al reporte los pacientes con estado "atendido".
  R2) Se ordena ASCENDENTE por prioridad (los críticos primero).
  R3) Si dos pacientes tienen la misma prioridad, debe quedar primero
      el que LLEGÓ ANTES (orden cronológico de ingreso). Esto importa
      porque el hospital evalúa tiempos de espera y el orden de atención
      esperado dentro de cada nivel de gravedad.

ANÁLISIS:
  1. Algoritmo elegido: Counting Sort
  2. Complejidad temporal con n=80,000 y k=5: O(n + k) → O(80,000 + 5)
  3. Complejidad espacial: O(n + k)
  4. Estabilidad: Sí, es estable. Es importante porque pacientes con igual
     prioridad deben conservar su orden cronológico de ingreso para poder
     auditar los tiempos de espera correctamente.

  Otros algoritmos descartados:
  - Quick Sort: inestable, rompe el orden de llegada entre pacientes iguales.
  - Heap Sort: inestable por la misma razón.
  - Merge Sort: estable y funciona, pero Counting Sort es más eficiente
    cuando k=5 es tan pequeño comparado con n.
  - Radix Sort: no tiene sentido con un rango tan pequeño.
"""


def ordenar_pacientes(pacientes):
    """
    Filtrar abandonos + ordenar por prioridad de forma estable.
    Algoritmo elegido: Counting Sort
    """
    solo_atendidos = []
    for pac in pacientes:
        if pac["estado"] == "atendido":
            solo_atendidos.append(pac)

    max_prioridad = 5
    frecuencia = [0] * (max_prioridad + 1)

    for pac in solo_atendidos:
        frecuencia[pac["prioridad"]] += 1

    for j in range(1, max_prioridad + 1):
        frecuencia[j] += frecuencia[j - 1]

    resultado = [None] * len(solo_atendidos)

    i = len(solo_atendidos) - 1
    while i >= 0:
        pri = solo_atendidos[i]["prioridad"]
        frecuencia[pri] -= 1
        resultado[frecuencia[pri]] = solo_atendidos[i]
        i -= 1

    return resultado



# ═══════════════════════════════════════════════════════════════════════════════
# CASO 2 (1.7): Ranking de Productos en E-commerce
# ═══════════════════════════════════════════════════════════════════════════════

"""
CONTEXTO:
---------
Una tienda en línea tiene 2 MILLONES de productos y debe ordenarlos por
RATING promedio para mostrarlos en la página principal. Al cierre de
cada día se reconstruye el ranking completo.

Cada producto es una tupla:

    (id_producto, rating, ventas_mes)
    # rating: float de 0.0 a 5.0 (con decimales)
    # ventas_mes: entero, ventas del último mes

RESTRICCIONES OPERACIONALES:
  R1) El servidor tiene RAM SUFICIENTE para usar memoria auxiliar.
  R2) El proceso debe ser PREDECIBLE.
  R3) Si dos productos tienen el mismo rating, debe respetarse el orden
      original (que viene priorizado por ventas del mes).

ANÁLISIS:
  1. Algoritmo elegido: Merge Sort
  2. Complejidad temporal: O(n log n) en peor caso y promedio
  3. Complejidad espacial: O(n)

  Otros algoritmos descartados:
  - Quick Sort: peor caso O(n²), no predecible. Tampoco es estable.
  - Heap Sort: no es estable, se pierde el orden por ventas en empates.
  - Counting Sort: los ratings son decimales, no se puede usar.
  - Radix Sort: no funciona con floats directamente.
"""


def mezclar(arreglo, inicio, mitad, fin):
    parte_izq = arreglo[inicio:mitad + 1]
    parte_der = arreglo[mitad + 1:fin + 1]

    a = 0
    b = 0
    k = inicio

    while a < len(parte_izq) and b < len(parte_der):
        if parte_izq[a][1] >= parte_der[b][1]:
            arreglo[k] = parte_izq[a]
            a += 1
        else:
            arreglo[k] = parte_der[b]
            b += 1
        k += 1

    while a < len(parte_izq):
        arreglo[k] = parte_izq[a]
        a += 1
        k += 1

    while b < len(parte_der):
        arreglo[k] = parte_der[b]
        b += 1
        k += 1


def ordenar_merge(arreglo, inicio, fin):
    if inicio < fin:
        mitad = (inicio + fin) // 2
        ordenar_merge(arreglo, inicio, mitad)
        ordenar_merge(arreglo, mitad + 1, fin)
        mezclar(arreglo, inicio, mitad, fin)


def ordenar_productos(lista):
    """
    Ordenar tuplas (id, rating, ventas) por rating descendente, estable.
    Algoritmo elegido: Merge Sort
    """
    copia = lista[:]
    ordenar_merge(copia, 0, len(copia) - 1)
    return copia


# ═══════════════════════════════════════════════════════════════════════════════
# CASO 3 (1.6): Sistema de Códigos de Barras EAN-13
# ═══════════════════════════════════════════════════════════════════════════════

"""
CONTEXTO:
---------
Una cadena de supermercados tiene 10 MILLONES de códigos de barras EAN-13
(números enteros de exactamente 13 dígitos) en su inventario y necesita
ordenarlos para compararlos contra el catálogo del proveedor y detectar
productos faltantes.

ESTRATEGIA OPERACIONAL:
  Paso A) Ordenar todos los códigos.
  Paso B) Recorrido lineal cruzando con el catálogo del proveedor.

RESTRICCIONES:
  R1) El rango es enorme (10^13), no se puede crear un arreglo de ese
      tamaño en memoria.
  R2) Se requiere tiempo CASI LINEAL.

ANÁLISIS:
  1. Algoritmo elegido: Radix Sort
  2. Complejidad temporal: O(d × (n + b)) → O(13 × (10,000,000 + 10))
  3. Complejidad espacial: O(n + b)

  Otros algoritmos descartados:
  - Counting Sort: rango de 10^13, necesitaría un arreglo gigante en memoria.
  - Quick Sort: O(n log n), no alcanza el tiempo casi lineal requerido.
  - Heap Sort: O(n log n), mismo problema.
  - Merge Sort: O(n log n), Radix es más rápido para enteros con pocos dígitos.
"""


def ordenar_por_posicion(arreglo, exponente):
    total = len(arreglo)
    resultado = [0] * total
    cuenta = [0] * 10

    for numero in arreglo:
        d = (numero // exponente) % 10
        cuenta[d] += 1

    for j in range(1, 10):
        cuenta[j] += cuenta[j - 1]

    i = total - 1
    while i >= 0:
        d = (arreglo[i] // exponente) % 10
        cuenta[d] -= 1
        resultado[cuenta[d]] = arreglo[i]
        i -= 1

    for i in range(total):
        arreglo[i] = resultado[i]


def ordenar_codigos(codigos):
    """
    Ordenar lista de enteros de 13 dígitos en tiempo casi lineal.
    Algoritmo elegido: Radix Sort
    """
    copia = codigos[:]
    valor_max = max(copia)
    exponente = 1

    while valor_max // exponente > 0:
        ordenar_por_posicion(copia, exponente)
        exponente *= 10

    return copia




# ═══════════════════════════════════════════════════════════════════════════════
# CÓDIGO DE PRUEBA
# ═══════════════════════════════════════════════════════════════════════════════

if __name__ == "__main__":
    print("=" * 60)
    print("PRUEBAS DEL QUIZ B DE ORDENAMIENTO")
    print("=" * 60)

    # CASO 1
    print("\n--- CASO 1: Triaje en Urgencias ---")
    pacientes = [
        {"id_atencion": 1, "paciente": "Maria",  "prioridad": 3, "hora_ingreso": "08:00", "estado": "atendido"},
        {"id_atencion": 2, "paciente": "Carlos", "prioridad": 1, "hora_ingreso": "08:05", "estado": "atendido"},
        {"id_atencion": 3, "paciente": "Lucia",  "prioridad": 3, "hora_ingreso": "08:10", "estado": "atendido"},
        {"id_atencion": 4, "paciente": "Pablo",  "prioridad": 2, "hora_ingreso": "08:15", "estado": "abandono"},
        {"id_atencion": 5, "paciente": "Sofia",  "prioridad": 1, "hora_ingreso": "08:20", "estado": "atendido"},
        {"id_atencion": 6, "paciente": "Diego",  "prioridad": 5, "hora_ingreso": "08:25", "estado": "atendido"},
    ]
    resultado = ordenar_pacientes(pacientes)
    if resultado:
        for p in resultado:
            print(f"  P{p['prioridad']} | {p['paciente']:7} | id={p['id_atencion']} | {p['hora_ingreso']}")
    else:
        print("  (sin implementar)")

    # CASO 2
    print("\n--- CASO 2: Ranking de productos ---")
    productos = [
        (101, 4.5, 320),
        (102, 3.8, 150),
        (103, 4.5, 410),
        (104, 5.0, 80),
        (105, 4.2, 600),
    ]
    resultado = ordenar_productos(productos)
    if resultado:
        for p in resultado:
            print(f"  ID {p[0]} | rating={p[1]} | ventas={p[2]}")
    else:
        print("  (sin implementar)")

    # CASO 3
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
    if resultado:
        for c in resultado:
            print(f"  {c}")
    else:
        print("  (sin implementar)")
