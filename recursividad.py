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

# ==========================================================
# QUIZ DE ANALISIS Y DISENO DE ALGORITMOS
# Tema: Complejidad temporal, espacial y Teorema Maestro
# ==========================================================

preguntas = [

    {
        "titulo": "PREGUNTA 1 - Ciclo simple",
        "codigo": """
def ejemplo(n):
    suma = 0

    for i in range(n):
        suma += i

    return suma
""",
        "pregunta": "¿Cual es la complejidad temporal?",
        "opciones": ["O(1)", "O(n)", "O(n^2)", "O(log n)"],
        "correcta": "O(n)",
        "razones": [
            "Porque el ciclo se ejecuta n veces.",
            "Porque hay dos ciclos anidados.",
            "Porque el valor se divide entre 2.",
            "Porque siempre realiza una operacion."
        ],
        "razon_correcta": 0,
        "explicacion": """
El ciclo for recorre todos los valores desde 0 hasta n-1.
Si n = 5, se ejecuta 5 veces.
Si n = 100, se ejecuta 100 veces.
El trabajo aumenta proporcionalmente a n.
Por eso es O(n).
"""
    },

    {
        "titulo": "PREGUNTA 2 - Ciclos anidados",
        "codigo": """
def ejemplo(n):
    contador = 0

    for i in range(n):
        for j in range(n):
            contador += 1

    return contador
""",
        "pregunta": "¿Cual es la complejidad temporal?",
        "opciones": ["O(n)", "O(n^2)", "O(n^3)", "O(log n)"],
        "correcta": "O(n^2)",
        "razones": [
            "Porque hay dos ciclos consecutivos.",
            "Porque hay dos ciclos anidados de n iteraciones.",
            "Porque solo se ejecuta una vez.",
            "Porque se divide n entre 2."
        ],
        "razon_correcta": 1,
        "explicacion": """
El primer ciclo se ejecuta n veces.
Por cada repeticion del primero, el segundo
tambien se ejecuta n veces.

Multiplicamos:
n * n = n^2.

Por eso es O(n^2).
"""
    },

    {
        "titulo": "PREGUNTA 3 - Ciclos consecutivos",
        "codigo": """
def ejemplo(n):
    contador = 0

    for i in range(n):
        contador += 1

    for j in range(n):
        contador += 1

    return contador
""",
        "pregunta": "¿Cual es la complejidad temporal?",
        "opciones": ["O(n)", "O(n^2)", "O(2^n)", "O(1)"],
        "correcta": "O(n)",
        "razones": [
            "Porque los ciclos estan anidados.",
            "Porque se suman n + n = 2n y se elimina la constante.",
            "Porque hay dos variables.",
            "Porque el segundo ciclo depende del primero."
        ],
        "razon_correcta": 1,
        "explicacion": """
Los ciclos NO estan anidados.
Primero se ejecuta uno y despues el otro.

El trabajo total es:
n + n = 2n.

En Big-O eliminamos las constantes.
Por eso O(2n) se convierte en O(n).
"""
    },

    {
        "titulo": "PREGUNTA 4 - Complejidad logaritmica",
        "codigo": """
def ejemplo(n):
    contador = 0

    while n > 1:
        n = n // 2
        contador += 1

    return contador
""",
        "pregunta": "¿Cual es la complejidad temporal?",
        "opciones": ["O(n)", "O(n^2)", "O(log n)", "O(1)"],
        "correcta": "O(log n)",
        "razones": [
            "Porque recorre todos los numeros.",
            "Porque n se reduce a la mitad en cada repeticion.",
            "Porque tiene dos ciclos.",
            "Porque no realiza operaciones."
        ],
        "razon_correcta": 1,
        "explicacion": """
En cada repeticion n se divide entre 2.

Ejemplo si n = 16:
16 -> 8 -> 4 -> 2 -> 1.

Solo necesita 4 repeticiones.
El numero de pasos crece de forma logaritmica.
Por eso es O(log n).
"""
    },

    {
        "titulo": "PREGUNTA 5 - Complejidad lineal logaritmica",
        "codigo": """
def ejemplo(n):
    contador = 0

    for i in range(n):
        j = n

        while j > 1:
            j = j // 2
            contador += 1

    return contador
""",
        "pregunta": "¿Cual es la complejidad temporal?",
        "opciones": ["O(n)", "O(log n)", "O(n log n)", "O(n^2)"],
        "correcta": "O(n log n)",
        "razones": [
            "Porque el ciclo externo se ejecuta n veces
y el interno log(n) veces.",
            "Porque solo hay un ciclo.",
            "Porque los dos ciclos se ejecutan n veces.",
            "Porque el ciclo interno nunca termina."
        ],
        "razon_correcta": 0,
        "explicacion": """
El ciclo externo se ejecuta n veces.

El ciclo interno divide j entre 2,
por lo que se ejecuta log(n) veces.

Multiplicamos:
n * log(n).

Por eso es O(n log n).
"""
    },

    {
        "titulo": "PREGUNTA 6 - Producto de variables",
        "codigo": """
def ejemplo(n, m):
    contador = 0

    for i in range(n):
        for j in range(m):
            contador += 1

    return contador
""",
        "pregunta": "¿Cual es la complejidad temporal?",
        "opciones": ["O(n + m)", "O(n * m)", "O(n^2)", "O(log n)"],
        "correcta": "O(n * m)",
        "razones": [
            "Porque los ciclos son consecutivos.",
            "Porque el primer ciclo depende de n
y el segundo depende de m.",
            "Porque ambos ciclos dependen solamente de n.",
            "Porque hay una sola operacion."
        ],
        "razon_correcta": 1,
        "explicacion": """
El ciclo externo se ejecuta n veces.
El ciclo interno se ejecuta m veces
por cada repeticion del externo.

Multiplicamos:
n * m.

Por eso es O(n * m).
No debemos asumir que m es igual a n.
"""
    },

    {
        "titulo": "PREGUNTA 7 - Termino dominante",
        "codigo": """
def ejemplo(n):
    for i in range(n):
        print(i)

    for i in range(n):
        for j in range(n):
            print(i, j)
""",
        "pregunta": "¿Cual es la complejidad total?",
        "opciones": ["O(n)", "O(n^2)", "O(n^3)", "O(2n)"],
        "correcta": "O(n^2)",
        "razones": [
            "Porque se suman n + n^2 y domina n^2.",
            "Porque se multiplican n * n^2.",
            "Porque solamente importa el primer ciclo.",
            "Porque se eliminan todos los ciclos."
        ],
        "razon_correcta": 0,
        "explicacion": """
El primer bloque cuesta O(n).
El segundo bloque cuesta O(n^2).

Sumamos:
O(n + n^2).

El termino que mas crece es n^2.
Por eso la complejidad final es O(n^2).
"""
    },

    {
        "titulo": "PREGUNTA 8 - Teorema Maestro",
        "codigo": """
T(n) = 2T(n/2) + n
""",
        "pregunta": "¿Cual es la complejidad?",
        "opciones": ["O(n)", "O(n log n)", "O(n^2)", "O(log n)"],
        "correcta": "O(n log n)",
        "razones": [
            "Porque a = 2, b = 2 y f(n) = n.
El resultado corresponde al caso de igualdad.",
            "Porque solo existe un llamado recursivo.",
            "Porque n siempre se duplica.",
            "Porque no hay trabajo fuera de la recursion."
        ],
        "razon_correcta": 0,
        "explicacion": """
Identificamos los valores:

a = 2: cantidad de llamados recursivos.
b = 2: el problema se divide entre 2.
f(n) = n: trabajo fuera de la recursion.

Calculamos:
n^(log_b(a)) = n^(log_2(2)) = n.

Como f(n) = n, estamos en el caso de igualdad.

Resultado:
O(n log n).
"""
    },

    {
        "titulo": "PREGUNTA 9 - Complejidad espacial",
        "codigo": """
def ejemplo(n):
    if n <= 1:
        return 1

    return n * ejemplo(n - 1)
""",
        "pregunta": "¿Cual es el espacio auxiliar debido a la recursion?",
        "opciones": ["O(1)", "O(log n)", "O(n)", "O(n^2)"],
        "correcta": "O(n)",
        "razones": [
            "Porque no hay llamadas recursivas.",
            "Porque la recursion genera hasta n llamadas
pendientes en el call stack.",
            "Porque hay dos ciclos anidados.",
            "Porque se divide el problema entre 2."
        ],
        "razon_correcta": 1,
        "explicacion": """
La funcion se llama a si misma con n - 1.

Por ejemplo:
ejemplo(5)
ejemplo(4)
ejemplo(3)
ejemplo(2)
ejemplo(1)

Se acumulan llamadas en el call stack.
La profundidad de la recursion es proporcional a n.

El espacio auxiliar es O(n).
"""
    },

    {
        "titulo": "PREGUNTA 10 - Arreglo auxiliar",
        "codigo": """
def ejemplo(n):
    lista = []

    for i in range(n):
        lista.append(i)

    return lista
""",
        "pregunta": "¿Cual es el espacio auxiliar utilizado?",
        "opciones": ["O(1)", "O(n)", "O(n^2)", "O(log n)"],
        "correcta": "O(n)",
        "razones": [
            "Porque solo se crea una variable.",
            "Porque la lista almacena n elementos adicionales.",
            "Porque el ciclo es constante.",
            "Porque no se utiliza memoria."
        ],
        "razon_correcta": 1,
        "explicacion": """
La lista comienza vacia.
En cada repeticion se agrega un elemento.

Si n = 5, guarda 5 elementos.
Si n = 100, guarda 100 elementos.

El espacio auxiliar crece proporcionalmente a n.
Por eso es O(n).
"""
    }
]


# ==========================================================
# FUNCION PARA VALIDAR RESPUESTAS
# ==========================================================

def pedir_respuesta(mensaje, cantidad):
    while True:
        respuesta = input(mensaje).strip()

        if respuesta.isdigit():
            numero = int(respuesta)

            if 1 <= numero <= cantidad:
                return numero

        print("Respuesta no valida. Intenta nuevamente.")


# ==========================================================
# INICIO DEL QUIZ
# ==========================================================

print("=" * 60)
print("       QUIZ DE COMPLEJIDAD ALGORITMICA")
print("=" * 60)

print("Instrucciones:")
print("1. Lee el codigo de cada ejercicio.")
print("2. Selecciona la complejidad correcta.")
print("3. Selecciona la razon que justifica tu respuesta.")
print("4. Al final conoceras tu calificacion.")
print("=" * 60)

puntaje = 0
total = len(preguntas)

for numero, p in enumerate(preguntas, start=1):

    print("\n" + "=" * 60)
    print(p["titulo"])
    print("=" * 60)

    print("\nCODIGO:")
    print(p["codigo"])

    print("\n" + p["pregunta"])

    print("\nOPCIONES:")

    for i, opcion in enumerate(p["opciones"], start=1):
        print(f"{i}. {opcion}")

    respuesta_complejidad = pedir_respuesta(
        "\nEscribe el numero de tu respuesta: ",
        len(p["opciones"])
    )

    seleccion = p["opciones"][respuesta_complejidad - 1]

    if seleccion == p["correcta"]:
        print("\n¡Correcto! La complejidad es", p["correcta"])
        puntaje += 1
    else:
        print("\nIncorrecto.")
        print("Tu respuesta:", seleccion)
        print("Respuesta correcta:", p["correcta"])

    # Ahora se pregunta por que esa complejidad es correcta.

    print("\nPERO... ¿POR QUE?")

    for i, razon in enumerate(p["razones"], start=1):
        print(f"\n{i}. {razon}")

    respuesta_razon = pedir_respuesta(
        "\nSelecciona la explicacion correcta: ",
        len(p["razones"])
    )

    if respuesta_razon - 1 == p["razon_correcta"]:
        print("\n¡Muy bien! Explicacion correcta.")
        puntaje += 1
    else:
        print("\nEsa no es la explicacion correcta.")
        print("La explicacion correcta es:")
        print(p["razones"][p["razon_correcta"]])

    print("\nEXPLICACION COMPLETA:")
    print(p["explicacion"])

    input("\nPresiona ENTER para continuar...")


# ==========================================================
# RESULTADO FINAL
# ==========================================================

puntos_maximos = total * 2
porcentaje = (puntaje / puntos_maximos) * 100

print("\n" + "=" * 60)
print("                 RESULTADOS FINALES")
print("=" * 60)

print("Preguntas realizadas:", total)
print("Puntos obtenidos:", puntaje, "de", puntos_maximos)
print("Porcentaje:", round(porcentaje, 2), "%")

if porcentaje >= 90:
    print("\n¡EXCELENTE! Estas muy bien preparado.")
elif porcentaje >= 70:
    print("\n¡BIEN! Tienes buenos conocimientos.")
elif porcentaje >= 50:
    print("\nVAS POR BUEN CAMINO. Debes practicar un poco mas.")
else:
    print("\nNECESITAS REPASAR. Vuelve a estudiar los ejemplos.")

print("=" * 60)
print("             FIN DEL QUIZ")
print("=" * 60)
