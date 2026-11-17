# =====================================================
# ANALISIS Y DISEÑO DE ALGORITMOS
# TEMA: COMPLEJIDAD ALGORITMICA
# =====================================================

# En este programa vamos a estudiar diferentes
# tipos de complejidad temporal (Big O).


# -----------------------------------------------------
# 1. COMPLEJIDAD O(1) - CONSTANTE
# -----------------------------------------------------

# ¿Por qué es O(1)?
# Porque realiza una cantidad fija de operaciones.
# No importa si n es 10, 100 o 1000.
# Siempre realiza una suma y devuelve el resultado.

def constante(n):
    resultado = n + 5
    return resultado


# -----------------------------------------------------
# 2. COMPLEJIDAD O(n) - LINEAL
# -----------------------------------------------------

# ¿Por qué es O(n)?
# Porque tiene un ciclo que se repite n veces.
# Si n = 5, se ejecuta 5 veces.
# Si n = 100, se ejecuta 100 veces.
# El trabajo crece proporcionalmente a n.

def lineal(n):
    contador = 0

    for i in range(n):
        contador += 1

    return contador


# -----------------------------------------------------
# 3. COMPLEJIDAD O(n^2) - CUADRATICA
# -----------------------------------------------------

# ¿Por qué es O(n^2)?
# Porque tiene dos ciclos anidados.
# El ciclo externo se repite n veces.
# El ciclo interno también se repite n veces
# por cada repetición del ciclo externo.
# Por eso multiplicamos n * n = n^2.

def cuadratica(n):
    contador = 0

    for i in range(n):
        for j in range(n):
            contador += 1

    return contador


# -----------------------------------------------------
# 4. COMPLEJIDAD O(n^3) - CUBICA
# -----------------------------------------------------

# ¿Por qué es O(n^3)?
# Porque tiene tres ciclos anidados.
# Cada ciclo se repite n veces.
# Multiplicamos n * n * n = n^3.

def cubica(n):
    contador = 0

    for i in range(n):
        for j in range(n):
            for k in range(n):
                contador += 1

    return contador


# -----------------------------------------------------
# 5. COMPLEJIDAD O(log n) - LOGARITMICA
# -----------------------------------------------------

# ¿Por qué es O(log n)?
# Porque en cada repetición dividimos n entre 2.
# El valor disminuye rápidamente.
# No recorre todos los números, sino que reduce
# el tamaño del problema a la mitad en cada paso.

def logaritmica(n):
    contador = 0

    while n > 1:
        n = n // 2
        contador += 1

    return contador


# -----------------------------------------------------
# 6. COMPLEJIDAD O(n log n) - LINEAL LOGARITMICA
# -----------------------------------------------------

# ¿Por qué es O(n log n)?
# Tiene un ciclo externo que se repite n veces.
# Dentro tiene un ciclo que divide n entre 2.
# El ciclo interno se ejecuta log(n) veces.
# Multiplicamos n * log(n).

def n_log_n(n):
    contador = 0

    for i in range(n):
        j = n

        while j > 1:
            j = j // 2
            contador += 1

    return contador


# -----------------------------------------------------
# 7. COMPLEJIDAD O(n * m) - PRODUCTO
# -----------------------------------------------------

# ¿Por qué es O(n * m)?
# Tiene dos ciclos anidados.
# El primer ciclo depende de n.
# El segundo ciclo depende de m.
# Multiplicamos n * m.
# Se utiliza cuando los ciclos tienen tamaños diferentes.

def producto(n, m):
    contador = 0

    for i in range(n):
        for j in range(m):
            contador += 1

    return contador


# -----------------------------------------------------
# 8. COMPLEJIDAD O(n) - SUMA DE CICLOS
# -----------------------------------------------------

# ¿Por qué es O(n)?
# Tenemos dos ciclos independientes o consecutivos.
# El primero realiza n operaciones.
# El segundo también realiza n operaciones.
# Sumamos: n + n = 2n.
# En Big O eliminamos las constantes.
# Resultado final: O(n).

def suma_ciclos(n):
    contador = 0

    for i in range(n):
        contador += 1

    for j in range(n):
        contador += 1

    return contador


# =====================================================
# EJECUCION DEL PROGRAMA
# =====================================================

# Definimos los valores de entrada.
n = 8
m = 5

print("======================================")
print("      ANALISIS DE COMPLEJIDAD")
print("======================================")

print("Valor de n:", n)
print("Valor de m:", m)

# Ejecutamos cada algoritmo y mostramos resultados.

print("\n1. COMPLEJIDAD O(1) - CONSTANTE")
print("Resultado:", constante(n))

print("\n2. COMPLEJIDAD O(n) - LINEAL")
print("Resultado:", lineal(n))

print("\n3. COMPLEJIDAD O(n^2) - CUADRATICA")
print("Resultado:", cuadratica(n))

print("\n4. COMPLEJIDAD O(n^3) - CUBICA")
print("Resultado:", cubica(n))

print("\n5. COMPLEJIDAD O(log n) - LOGARITMICA")
print("Resultado:", logaritmica(n))

print("\n6. COMPLEJIDAD O(n log n)")
print("Resultado:", n_log_n(n))

print("\n7. COMPLEJIDAD O(n*m) - PRODUCTO")
print("Resultado:", producto(n, m))

print("\n8. COMPLEJIDAD O(n) - SUMA DE CICLOS")
print("Resultado:", suma_ciclos(n))

print("\n======================================")
print("          FIN DEL PROGRAMA")
print("======================================")
