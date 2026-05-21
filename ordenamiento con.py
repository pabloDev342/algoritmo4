# =========================================================
# ALGORITMOS DE ORDENAMIENTO - QUIZ COMPLETO
# =========================================================
#
# Autor: Estudio para quiz
#
# Este archivo contiene ejemplos de:
#
# 1. Counting Sort
# 2. Heap Sort
# 3. Merge Sort
# 4. Radix Sort
# 5. Bucket Sort
#
# Cada algoritmo incluye:
# - explicación
# - complejidad
# - ventajas
# - desventajas
# - cuándo usarlo
# - cuándo NO usarlo
#
# =========================================================



# =========================================================
# CASO 1 - COUNTING SORT
# Sistema de notas universitarias
# =========================================================

# ¿Por qué usar Counting Sort?
#
# Porque:
# - las notas son enteros
# - rango pequeño (0-100)
# - necesitamos estabilidad
#
# Complejidad:
# Tiempo -> O(n + k)
# Espacio -> O(n + k)
#
# n = cantidad de estudiantes
# k = rango de notas posibles


def counting_sort(arr):

    # Rango máximo de notas
    k = 101

    # Array para contar frecuencias
    count = [0] * k

    # Array de salida
    output = [0] * len(arr)

    # Contamos cuántas veces aparece cada nota
    for num in arr:
        count[num] += 1

    # Convertimos frecuencias en posiciones
    for i in range(1, k):
        count[i] += count[i - 1]

    # Recorremos al revés para mantener estabilidad
    for i in range(len(arr) - 1, -1, -1):

        num = arr[i]

        output[count[num] - 1] = num

        count[num] -= 1

    return output


print("\n================ COUNTING SORT ================\n")

notas = [90, 70, 100, 70, 85, 90]

resultado = counting_sort(notas)

print("Notas ordenadas:")
print(resultado)

# ¿Por qué NO usar Quick Sort?
#
# Porque Quick Sort es O(n log n)
# mientras Counting Sort puede ser O(n)
#
# Cuando k es pequeño, Counting Sort es mejor.



# =========================================================
# CASO 2 - HEAP SORT
# Sistema bancario / poca memoria
# =========================================================

# ¿Por qué usar Heap Sort?
#
# Porque:
# - usa O(1) memoria extra
# - es IN-PLACE
# - garantiza O(n log n)
# - no tiene peor caso O(n²)
#
# Ideal para:
# - servidores
# - producción
# - sistemas embebidos


def heapify(arr, n, i):

    largest = i

    left = 2 * i + 1
    right = 2 * i + 2

    # Verificamos hijo izquierdo
    if left < n and arr[left] > arr[largest]:
        largest = left

    # Verificamos hijo derecho
    if right < n and arr[right] > arr[largest]:
        largest = right

    # Si el mayor cambió
    if largest != i:

        # Intercambiamos
        arr[i], arr[largest] = arr[largest], arr[i]

        # Heapify recursivo
        heapify(arr, n, largest)


def heap_sort(arr):

    n = len(arr)

    # Construimos max heap
    for i in range(n // 2 - 1, -1, -1):
        heapify(arr, n, i)

    # Extraemos elementos
    for i in range(n - 1, 0, -1):

        arr[i], arr[0] = arr[0], arr[i]

        heapify(arr, i, 0)


print("\n================ HEAP SORT ================\n")

transacciones = [5000, 200, 15000, 7000, 100]

heap_sort(transacciones)

print("Transacciones ordenadas:")
print(transacciones)

# ¿Por qué NO usar Merge Sort?
#
# Porque Merge Sort necesita memoria extra O(n)
#
# Heap Sort usa O(1)



# =========================================================
# CASO 3 - MERGE SORT
# RRHH - mantener orden previo
# =========================================================

# ¿Por qué usar Merge Sort?
#
# Porque:
# - es ESTABLE
# - mantiene orden previo
# - garantiza O(n log n)
#
# Ideal cuando:
# - hay múltiples criterios
# - necesitamos estabilidad


def merge_sort(arr):

    if len(arr) > 1:

        mid = len(arr) // 2

        left = arr[:mid]
        right = arr[mid:]

        # División recursiva
        merge_sort(left)
        merge_sort(right)

        i = j = k = 0

        # Mezclamos ordenadamente
        while i < len(left) and j < len(right):

            # Ordenamos por departamento
            if left[i][0] < right[j][0]:

                arr[k] = left[i]
                i += 1

            else:

                arr[k] = right[j]
                j += 1

            k += 1

        # Elementos restantes
        while i < len(left):

            arr[k] = left[i]
            i += 1
            k += 1

        while j < len(right):

            arr[k] = right[j]
            j += 1
            k += 1


print("\n================ MERGE SORT ================\n")

empleados = [

    ("Ventas", "Carlos"),
    ("Sistemas", "Ana"),
    ("Ventas", "Luis"),
    ("RRHH", "Maria")

]

merge_sort(empleados)

print("Empleados ordenados:")
print(empleados)

# ¿Por qué NO usar Heap Sort?
#
# Porque Heap Sort NO es estable.
#
# Podría romper el orden previo.



# =========================================================
# CASO 4 - RADIX SORT
# Cédulas / IDs grandes
# =========================================================

# ¿Por qué usar Radix Sort?
#
# Porque:
# - los números tienen muchos dígitos
# - el rango es enorme
# - Counting Sort consumiría demasiada memoria
#
# Radix ordena dígito por dígito.
#
# Complejidad:
# O(d * (n + k))


def counting_sort_digit(arr, exp):

    n = len(arr)

    output = [0] * n

    count = [0] * 10

    # Contamos ocurrencias
    for num in arr:

        index = (num // exp) % 10

        count[index] += 1

    # Acumulamos
    for i in range(1, 10):
        count[i] += count[i - 1]

    # Construimos salida estable
    for i in range(n - 1, -1, -1):

        index = (arr[i] // exp) % 10

        output[count[index] - 1] = arr[i]

        count[index] -= 1

    # Copiamos
    for i in range(n):
        arr[i] = output[i]


def radix_sort(arr):

    max_num = max(arr)

    exp = 1

    while max_num // exp > 0:

        counting_sort_digit(arr, exp)

        exp *= 10


print("\n================ RADIX SORT ================\n")

cedulas = [1234567890, 3456789012, 1111111111, 2222222222]

radix_sort(cedulas)

print("Cédulas ordenadas:")
print(cedulas)

# ¿Por qué NO usar Counting Sort directo?
#
# Porque el rango llega hasta 10^10
#
# Necesitaríamos demasiada memoria.



# =========================================================
# CASO 5 - BUCKET SORT
# Distribución uniforme
# =========================================================

# ¿Por qué usar Bucket Sort?
#
# Porque:
# - la distribución es uniforme
# - los datos se reparten bien
#
# Bucket Sort aprovecha eso.
#
# Complejidad promedio:
# O(n + k)
#
# PERO:
# si la distribución NO es uniforme
# puede caer a O(n²)


def bucket_sort(arr):

    bucket_count = 10

    buckets = [[] for _ in range(bucket_count)]

    max_value = max(arr)

    # Distribuimos elementos
    for num in arr:

        index = int(num * bucket_count / (max_value + 1))

        buckets[index].append(num)

    # Ordenamos cada bucket
    for bucket in buckets:
        bucket.sort()

    # Unimos buckets
    result = []

    for bucket in buckets:
        result.extend(bucket)

    return result


print("\n================ BUCKET SORT ================\n")

datos = [78, 17, 39, 26, 72, 94, 21]

resultado = bucket_sort(datos)

print("Datos ordenados:")
print(resultado)

# ¿Por qué NO usar Counting Sort?
#
# Porque k puede ser demasiado grande.
#
# Bucket Sort aprovecha mejor la distribución uniforme.



# =========================================================
# QUICK SORT (SOLO REFERENCIA)
# =========================================================

# Quick Sort suele ser rápido en promedio.
#
# PERO:
# - NO es estable
# - puede caer a O(n²)
#
# NO se recomienda cuando:
# - hay datos casi ordenados
# - producción necesita garantías
# - estabilidad es importante



# =========================================================
# RESUMEN FINAL
# =========================================================

print("\n================ RESUMEN FINAL ================\n")

print("1. Enteros + rango pequeño -> Counting Sort")
print("2. Poca memoria -> Heap Sort")
print("3. Estabilidad -> Merge Sort")
print("4. Muchos dígitos -> Radix Sort")
print("5. Distribución uniforme -> Bucket Sort")



# =========================================================
# TABLA MENTAL PARA EL QUIZ
# =========================================================

#
# Si el problema menciona...
#
# - rango pequeño -> Counting
# - estabilidad -> Merge
# - poca RAM -> Heap
# - muchos dígitos -> Radix
# - distribución uniforme -> Bucket
#
# Evita Quick Sort cuando:
#
# - datos casi ordenados
# - producción
# - peor caso importante
#
# =========================================================