# 🎯 Elección del Algoritmo de Ordenamiento

## Tabla de referencia

| Algoritmo      | Mejor    | Promedio  | Peor      | Espacio  | Estable | Notas |
|----------------|----------|-----------|-----------|----------|---------|-------|
| Merge Sort     | O(n log n) | O(n log n) | O(n log n) | O(n)     | ✅ Sí   | Garantiza n log n siempre |
| Quick Sort     | O(n log n) | O(n log n) | O(n²)     | O(log n) | ❌ No   | Rápido en práctica, in-place |
| Heap Sort      | O(n log n) | O(n log n) | O(n log n) | O(1)     | ❌ No   | In-place, sin peor caso malo |
| Counting Sort  | O(n + k) | O(n + k)  | O(n + k)  | O(n + k) | ✅ Sí   | Solo enteros con rango limitado k |
| Radix Sort     | O(d(n+k)) | O(d(n+k)) | O(d(n+k)) | O(n + k) | ✅ Sí   | Para enteros/strings de d dígitos |
| Bucket Sort    | O(n + k) | O(n + k)  | O(n²)     | O(n + k) | ✅ Sí*  | Datos uniformemente distribuidos |

---

## 🧩 10 Casos para que los estudiantes decidan

Para cada caso analiza:
1. ¿Cuál es el mejor algoritmo? ¿Por qué?
2. ¿Qué algoritmos descartas y por qué?
3. Considera complejidad temporal, espacial y estabilidad
4. ¿Qué pasaría si cambian alguna restricción del problema?

---

### Caso 1: Sistema de notas finales de un semestre universitario

**Contexto del problema:**
La universidad necesita generar el listado oficial de calificaciones al final
del semestre. Tienes una base de datos con 200 estudiantes de un curso, cada
uno con una nota final en escala 0-100 (números enteros). El sistema debe
imprimir el listado ordenado de menor a mayor para publicarlo en la cartelera
oficial.

**Datos clave:**
- Tamaño: n = 200 estudiantes
- Tipo de dato: enteros entre 0 y 100
- Rango: k = 101 valores posibles (muy pequeño)
- Restricción: si dos estudiantes tienen la misma nota, deben quedar en el
  orden en que aparecen en la lista original (orden alfabético previo).
- No hay limitación de memoria.

**Pregunta:**
¿Qué algoritmo eliges? Justifica considerando complejidad temporal, espacial
y la necesidad de estabilidad. ¿Cambiaría tu respuesta si fueran 10 millones
de estudiantes en lugar de 200?

---

### Caso 2: Cierre diario de un sistema bancario

**Contexto del problema:**
Un banco mediano procesa cerca de 1 millón de transacciones diarias. Al cierre
del día, el equipo de auditoría necesita una lista ordenada por monto para
detectar anomalías y generar reportes regulatorios. El servidor que ejecuta
este proceso es compartido con otros sistemas críticos, por lo que **NO puede
consumir más de 500 MB de RAM extra** durante el ordenamiento.

**Datos clave:**
- Tamaño: n = 1,000,000 transacciones
- Tipo de dato: números reales (decimales) en pesos colombianos
- Rango: desde 100 hasta 10,000,000,000 (10^10) → rango enorme
- Restricción de memoria: poca RAM extra disponible
- Restricción de tiempo: el reporte debe estar listo en menos de 5 minutos
- No se requiere estabilidad (cada transacción tiene un ID único)
- El proceso se ejecuta en producción, por lo que **NO se aceptan sorpresas
  con peores casos malos**.


---

### Caso 3: Limpieza de archivos en un servidor de producción

**Contexto del problema:**
Eres administrador de un servidor con 50,000 archivos. Necesitas ordenarlos
por tamaño para identificar los más grandes y liberar espacio. El servidor
ejecuta este proceso durante la madrugada como tarea programada y **debe
terminar en una ventana fija de 30 minutos**, sin importar la distribución de
los datos. No puedes permitir que el algoritmo se demore más de lo previsto.

**Datos clave:**
- Tamaño: n = 50,000 archivos
- Tipo de dato: enteros (bytes), desde 1KB (1024) hasta 10GB (10^10)
- Distribución: muy variada e impredecible
- Restricción crítica: garantía de tiempo en el peor caso
- Memoria: disponible (servidor de producción con buena RAM)
- Estabilidad: no requerida



---

### Caso 4: Reportes de RRHH ordenados por dos criterios

**Contexto del problema:**
El área de Recursos Humanos te pide un reporte de empleados ordenado por
DEPARTAMENTO. El detalle: dentro de cada departamento, los empleados deben
aparecer ordenados por SALARIO (de mayor a menor). Tú ya tienes la lista
ordenada por salario (descendente). Lo único que falta es agruparlos por
departamento manteniendo el orden previo.

**Datos clave:**
- Tamaño: n = 5,000 empleados
- La lista de entrada YA está ordenada por salario descendente
- Necesitas reordenar por departamento, **manteniendo el orden por salario
  dentro de cada departamento**
- Departamentos: aproximadamente 15 distintos
- Memoria: disponible

---

### Caso 5: Detección de cédulas duplicadas en una base nacional

**Contexto del problema:**
La Registraduría te entrega un archivo con 10 millones de cédulas (números
enteros) y te pide ordenarlas para detectar duplicados. Las cédulas
colombianas tienen hasta 10 dígitos (1 a 9,999,999,999). Tienes que procesar
todo en una máquina con 16 GB de RAM: el
proceso anterior tardaba más de una hora y se
necesita reducirlo significativamente.

**Datos clave:**
- Tamaño: n = 10,000,000 cédulas
- Tipo de dato: enteros de hasta 10 dígitos (d = 10)
- Rango: hasta 10^10 → demasiado grande para Counting Sort directo
- Memoria: amplia (16 GB)
- Estabilidad: deseable para auditoría


---

### Caso 6: Sensor IoT de temperatura en un microcontrolador

**Contexto del problema:**
Estás programando el firmware de un sensor de temperatura para uso industrial.
El microcontrolador tiene **apenas 4 KB de RAM total** y debe almacenar 100
mediciones de temperatura del último día para luego ordenarlas y enviar la
mediana al servidor central. Cualquier algoritmo que use memoria extra
significativa hará que el dispositivo falle por desbordamiento de memoria.

**Datos clave:**
- Tamaño: n = 100 mediciones
- Tipo de dato: enteros (la temperatura va de -40 a 85, multiplicada por 100)
- Rango: ~12,500 valores posibles
- Estabilidad: no relevante


**Pregunta:**
¿Qué algoritmo eliges considerando que la memoria es la restricción más dura?
¿Por qué Merge Sort no funciona aquí? ¿Por qué Counting Sort tampoco es buena
idea aunque los datos sean enteros? ¿Qué algoritmo es completamente in-place
y aún así garantiza O(n log n)?

---

### Caso 7: Stream de datos de un sensor en tiempo real

**Contexto del problema:**
Tienes un sistema de monitoreo ambiental que recibe 1 medición por segundo
durante todo el día. Cada medición es un valor entero entre 0 y 100 (índice
de calidad del aire). Al final del día (86,400 segundos ≈ 86,400 mediciones)
debes ordenar todo el batch para generar estadísticas. Como las mediciones se
repetirán mucho (rango pequeño), buscas el algoritmo más rápido posible.

**Datos clave:**
- Tamaño: n ≈ 86,400 mediciones por día
- Tipo de dato: enteros entre 0 y 100
- Rango: k = 101 (muy pequeño comparado con n)
- Memoria: disponible (es un servidor)
- Estabilidad: deseable para mantener orden temporal

**Pregunta:**
¿Qué algoritmo permite ordenar en tiempo lineal O(n)? ¿Por qué los algoritmos
basados en comparación (Merge/Heap/Quick) son innecesariamente lentos aquí?
Si el rango fuera 0 a 1,000,000 en lugar de 0 a 100, ¿cambiarías de
algoritmo? ¿Cuál escogerías?

---

### Caso 8: Distribución de paquetes en una empresa de logística

**Contexto del problema:**
Una empresa de envíos como Servientrega tiene 500,000 paquetes que llegan a
un centro de distribución y deben clasificarse por código postal para enviarse
a la región correcta. Los códigos postales en Colombia son enteros de 6
dígitos (000000 a 999999). El equipo de operaciones ha verificado que la
**distribución de paquetes por código postal es bastante uniforme**: ningún
código concentra más del 1% de los paquetes.

**Datos clave:**
- Tamaño: n = 500,000 paquetes
- Tipo de dato: enteros de 6 dígitos
- Rango: 0 a 999,999 → k = 1,000,000
- Distribución: **uniforme** (información clave del problema)
- Memoria: disponible
- Estabilidad: no requerida

**Pregunta:**
¿Qué algoritmo aprovecha específicamente la "distribución uniforme"? ¿Por qué
NO es buena idea Counting Sort aunque sean enteros (pista: compara n vs k)?
¿Qué pasa si la distribución NO fuera uniforme y todos los paquetes vinieran
de unos pocos códigos? ¿A qué algoritmo te cambiarías?

---

### Caso 9: Cola de procesos en un sistema operativo

**Contexto del problema:**
Estás implementando el planificador de procesos de un sistema operativo
sencillo. Tienes 10,000 procesos en cola, cada uno con:
- Una **prioridad** (entero del 1 al 10, donde 10 es lo más urgente)
- Un **nombre** del proceso
- Un **timestamp** de cuándo llegó

Necesitas ordenarlos por prioridad descendente. Cuando dos procesos tienen la
misma prioridad, deben atenderse **en el orden de llegada** (FIFO dentro de
cada prioridad).

**Datos clave:**
- Tamaño: n = 10,000 procesos
- Tipo de dato: prioridades enteras 1-10 (k = 10)
- Restricción crítica: estabilidad obligatoria (orden de llegada)
- Memoria: disponible
- Tiempo: lo más rápido posible (es un planificador en tiempo real)

**Pregunta:**
¿Qué algoritmo te da O(n) y mantiene el orden de llegada? Mucha gente respondería
"Heap Sort porque es una cola de prioridad", pero esa respuesta es incorrecta
para este caso. ¿Por qué? ¿Cuál es la diferencia entre "ordenar un batch de
prioridades" y "mantener una cola de prioridad dinámica"?

---

### Caso 10: Catálogo de productos en una plataforma e-commerce

**Contexto del problema:**
Mercado Libre necesita ordenar alfabéticamente 100,000 nombres de productos
para mostrar el catálogo en la sección "navegar por nombre". Los nombres son
strings de hasta 50 caracteres con tildes y caracteres especiales. El catálogo
se actualiza una vez al día y se cachea, por lo que el tiempo no es crítico
pero sí debe ser predecible. Tienes memoria de sobra en el servidor.

**Datos clave:**
- Tamaño: n = 100,000 productos
- Tipo de dato: strings de hasta 50 caracteres
- Memoria: amplia
- Restricción: tiempo predecible (no se aceptan picos de O(n²))
- Estabilidad: deseable (los productos vienen pre-ordenados por categoría)

**Pregunta:**
¿Por qué Counting Sort, Radix Sort y Bucket Sort no son la primera opción para
strings largos? Entre Merge Sort, Heap Sort y Quick Sort: ¿cuál combina
estabilidad + garantía de O(n log n)? ¿Qué desventaja tiene Quick Sort cuando
los strings ya vienen casi ordenados (por ejemplo, ordenados por categoría)?

---

# ═════════════════════════════════════════════════════════════════════════════
# 💡 SOLUCIONES DETALLADAS
# ═════════════════════════════════════════════════════════════════════════════

## ✅ Caso 1: Notas finales — **Counting Sort**

**Análisis del problema:**
Tenemos n = 200 enteros en un rango muy pequeño (k = 101). Estamos en un
escenario perfecto para los algoritmos NO comparativos.

**¿Por qué Counting Sort?**
- Tiempo: O(n + k) = O(200 + 101) ≈ O(n). Lineal y muy rápido.
- Espacio: O(n + k), aceptable porque k es pequeño (101 contadores).
- Estabilidad: ✅ es estable, lo que respeta el orden alfabético previo cuando
  hay empates en la nota.

**¿Por qué NO los demás?**
- Merge/Quick/Heap Sort son O(n log n). Funcionan, pero son innecesariamente
  lentos cuando el rango es pequeño.
- Radix Sort funcionaría pero es overkill: las notas tienen pocos dígitos y
  Counting Sort es más simple y rápido.
- Bucket Sort también funcionaría, pero al ser enteros con rango fijo,
  Counting Sort es la elección más natural.

**¿Y si fueran 10 millones de estudiantes?**
La respuesta NO cambia: Counting Sort sigue siendo O(n + k) = O(10^7 + 101) ≈
O(n). Mientras k siga siendo pequeño respecto a n, Counting Sort es imbatible.
Solo cambiaría si las notas fueran reales con muchos decimales (ahí
necesitaríamos Bucket Sort o Quick/Merge).

---

## ✅ Caso 2: Sistema bancario — **Heap Sort**

**Análisis del problema:**
1 millón de números reales con rango enorme (10^10), memoria limitada y
necesidad de garantía de tiempo en producción. Las restricciones eliminan
varios candidatos.

**¿Por qué Heap Sort?**
- Tiempo: O(n log n) **garantizado** en peor caso (~20 millones de
  comparaciones para n = 10^6).
- Espacio: O(1) → es **in-place**, no consume RAM extra.
- Sin sorpresas en producción: nunca degrada a O(n²).

**¿Por qué NO los demás?**
- **Counting/Radix/Bucket**: descartados porque los datos son reales con rango
  enorme. No se pueden usar directamente.
- **Merge Sort**: tiempo bueno pero usa O(n) de memoria extra → 1 millón de
  flotantes ocupan más RAM de la disponible.
- **Quick Sort**: en promedio es más rápido, pero su peor caso O(n²) es
  inaceptable en producción. Si el dataset trae un patrón que cae en su peor
  caso (datos casi ordenados), el cierre del día se haría lentísimo.

**Comparación práctica:**
- Merge Sort: ~20M operaciones + 1M de RAM extra (no hay)
- Heap Sort: ~20M operaciones + 0 RAM extra → ¡gana!
- Quick Sort: ~20M operaciones promedio, pero hasta 10^12 en peor caso → riesgo

---

## ✅ Caso 3: Limpieza de archivos — **Heap Sort** (o Merge Sort)

**Análisis del problema:**
La palabra clave es **"predecibilidad"**. El proceso debe terminar en tiempo
fijo sin importar la entrada.

**¿Por qué Heap Sort o Merge Sort?**
Ambos garantizan O(n log n) en el peor caso. Para n = 50,000:
- ~50,000 × log2(50,000) ≈ 50,000 × 16 ≈ 800,000 operaciones.
- Esto es muy rápido y predecible.

**¿Cuál de los dos elegir?**
| Criterio | Merge Sort | Heap Sort |
|----------|------------|-----------|
| Tiempo | O(n log n) | O(n log n) |
| Espacio | O(n) extra | O(1) in-place |
| Estabilidad | ✅ | ❌ |
| Velocidad real | Suele ser más rápido | Un poco más lento por saltos en memoria |

Como **NO se requiere estabilidad** y la memoria está disponible, ambos son
válidos. **Heap Sort** gana ligeramente por usar menos memoria, pero **Merge
Sort** suele ser un poco más rápido en la práctica por mejor uso del caché.

**¿Por qué NO Quick Sort?**
Aunque suele ser el más rápido en promedio, tiene peor caso O(n²). Si los
archivos ya vienen casi ordenados por tamaño (caso común con archivos de un
mismo tipo), Quick Sort se cae a O(n²). Para n = 50,000 eso sería 2,500
millones de operaciones → minutos de demora extra. Inaceptable cuando hay
ventana fija.

---

## ✅ Caso 4: RRHH por dos criterios — **Merge Sort**

**Análisis del problema:**
Este es un caso clásico de "ordenamiento por múltiples claves usando
estabilidad". La estrategia es:
1. Ya está ordenado por la clave secundaria (salario).
2. Se aplica un algoritmo **estable** sobre la clave primaria (departamento).
3. Como es estable, los empates en departamento mantienen el orden por salario.

**¿Por qué Merge Sort?**
- ✅ Es **estable** → respeta el orden previo cuando hay empates.
- O(n log n) garantizado.
- Memoria disponible, así que el O(n) extra no es problema.

**¿Por qué NO Quick Sort y Heap Sort?**
Ambos son **inestables**. Si los aplicas, dentro de cada departamento el orden
por salario puede romperse y los empleados aparecerían en orden aleatorio.
Esto rompe el requisito del reporte.

**¿Counting Sort funcionaría?**
Sí, sería incluso mejor. Como solo hay ~15 departamentos (k = 15 muy pequeño
comparado con n = 5,000), Counting Sort sería O(n + k) ≈ O(n) y es estable.
La respuesta más completa es: **"Counting Sort si el número de departamentos
es pequeño y conocido, sino Merge Sort"**.

**Truco mnemotécnico:** "Si el problema dice 'ordenar manteniendo el orden
previo', necesitas un algoritmo ESTABLE. Punto."

---

## ✅ Caso 5: Cédulas duplicadas — **Radix Sort**

**Análisis del problema:**
Tenemos enteros con rango enorme (10^10) y cantidad gigante (10^7). Counting
Sort directo necesitaría un array de 10^10 contadores → imposible. Pero
Counting Sort aplicado **dígito por dígito** sí funciona: ese es Radix Sort.

**¿Por qué Radix Sort?**
- Tiempo: O(d × (n + k)) donde d=10 dígitos y k=10 (base decimal)
  = O(10 × (10^7 + 10)) ≈ O(10^8) → unas 100 millones de operaciones.
- Comparado con O(n log n) = 10^7 × 23 ≈ 2.3 × 10^8 operaciones.
- Radix es ~2x más rápido en este caso, **y es estable**.

**¿Por qué NO Counting Sort directo?**
Counting Sort necesita un array auxiliar de tamaño k. Con k = 10^10,
necesitaríamos 80 GB de memoria solo para los contadores. Imposible.

**¿Por qué NO Quick/Heap Sort?**
Funcionan, pero son O(n log n) sin la posibilidad de bajar más. Radix Sort
explota la estructura de los datos (que son enteros con pocos dígitos) para
romper esa barrera.

**Cálculo real:**
- O(n log n) ≈ 10^7 × 23 = 230 millones de comparaciones
- O(d × n) ≈ 10 × 10^7 = 100 millones de operaciones simples
- Radix gana incluso considerando las constantes ocultas.

---

## ✅ Caso 6: Sensor IoT — **Heap Sort**

**Análisis del problema:**
La restricción crítica es **memoria**: 4 KB de RAM. Cualquier algoritmo que
use O(n) extra está descartado.

**¿Por qué Heap Sort?**
- Es **in-place** → O(1) memoria extra. Es decir, no necesita un segundo
  arreglo, modifica el original.
- Garantiza O(n log n). Para n=100, eso es ~700 operaciones, instantáneo.
- No tiene peor caso malo.

**¿Por qué NO los demás?**
- **Counting Sort**: necesita un array de 12,500 contadores (rango k). Si cada
  entero ocupa 2 bytes, son 25 KB → no caben en 4 KB.
- **Merge Sort**: usa O(n) memoria extra para el buffer de merge → si bien para
  n=100 son solo 200 bytes, en este tipo de hardware todo cuenta y Heap Sort
  no necesita absolutamente nada.
- **Bucket/Radix**: necesitan memoria para las cubetas, descartados.
- **Quick Sort**: usa O(log n) por la pila de recursión y tiene peor caso
  malo. Para sistemas embebidos donde todo debe ser predecible, no se usa.

**Curiosidad:** Heap Sort es el algoritmo preferido en sistemas embebidos y
en kernels de sistemas operativos justamente por estas razones (memoria
mínima + peor caso garantizado).

---

## ✅ Caso 7: Stream de datos — **Counting Sort**

**Análisis del problema:**
86,400 valores enteros con rango k = 101. Caso ideal para Counting Sort.

**¿Por qué Counting Sort?**
- Tiempo: O(n + k) = O(86,500) ≈ O(n). Lineal.
- Como las mediciones SE REPITEN MUCHO (k=101 pero n=86,400), Counting Sort
  agrupa todo en 101 contadores sin tener que comparar.
- Es estable → mantiene el orden temporal de las mediciones.

**¿Por qué los algoritmos comparativos son innecesariamente lentos?**
- Merge/Heap/Quick Sort: O(n log n) = 86,400 × 17 ≈ 1.5 millones de
  comparaciones.
- Counting Sort: ~86,500 operaciones simples (incrementos en un array).
- ~17x más rápido. Para un sistema que se ejecuta diariamente, esa diferencia
  importa.

**¿Y si el rango fuera 0 a 1,000,000?**
Entonces n = 86,400 y k = 10^6 → k > n. Counting Sort se vuelve ineficiente
(usa más memoria que el propio dataset). En ese caso usaría:
- **Radix Sort** si los datos son enteros (sigue siendo O(n) si d es pequeño).
- **Bucket Sort** si la distribución es uniforme.
- **Heap/Merge Sort** si nada de lo anterior aplica → O(n log n).

---

## ✅ Caso 8: Logística — **Bucket Sort** (o Radix Sort)

**Análisis del problema:**
La pista crítica es **"distribución uniforme"**. Bucket Sort fue diseñado
exactamente para este caso.

**¿Por qué Bucket Sort?**
- Tiempo promedio: O(n + k) cuando la distribución es uniforme.
- Estrategia: divide los códigos postales en cubetas (por ejemplo, 1000
  cubetas de 1000 códigos cada una). Como la distribución es uniforme, cada
  cubeta queda con ~500 elementos. Ordenas cada cubeta con un algoritmo simple
  (insertion sort) y concatenas.
- Es estable.

**¿Por qué NO Counting Sort directo?**
- Necesitaría 1,000,000 contadores (uno por cada código postal posible).
- Comparar n=500,000 vs k=1,000,000: k > n, ineficiente. Más memoria gastada
  en contadores que en los datos mismos.

**¿Y si la distribución NO fuera uniforme?**
Bucket Sort se degrada a O(n²) en el peor caso (todos los elementos en una
sola cubeta). Por eso la pista de "distribución uniforme" es clave.

Si NO supiéramos si es uniforme, la mejor opción sería **Radix Sort**:
O(d × n) = O(6 × 500,000) ≈ O(n), garantizado sin importar la distribución.
Es la opción "segura" para enteros.

**Decisión final:**
- "Distribución uniforme" mencionada → **Bucket Sort** (aprovecha la pista).
- "Sin información sobre distribución" → **Radix Sort** (más seguro).

---

## ✅ Caso 9: Cola de procesos — **Counting Sort**

**Análisis del problema:**
Trampa del enunciado: muchos estudiantes responden "Heap Sort" porque la
palabra "prioridad" hace pensar en heaps. **Esa respuesta es incorrecta** para
ordenar un batch.

**¿Por qué Counting Sort?**
- Las prioridades son enteros 1-10 → k = 10, muy pequeño.
- Tiempo: O(n + k) = O(10,010) ≈ O(n). Lineal.
- Es **estable** → mantiene el orden de llegada (FIFO) cuando hay empates.

**¿Por qué Heap Sort NO es la respuesta correcta aquí?**
Esta es la diferencia clave que confunde a muchos:

| Cola de prioridad dinámica | Ordenar batch de prioridades |
|---------------------------|------------------------------|
| Insertar/extraer continuamente | Ordenar todo de una vez |
| Heap Sort / Priority Queue (heapq) | Counting Sort (si k pequeño) |
| O(log n) por operación | O(n + k) total |
| **NO es estable** | **Sí es estable** |

Para "tener procesos llegando y atendiéndolos uno por uno" usarías un heap
(estructura de datos). Pero para "ordenar 10,000 procesos de una vez", Counting
Sort es más rápido.

Además, Heap Sort no es estable → rompería el orden FIFO entre procesos con
la misma prioridad. Inaceptable según el enunciado.

**Para descartar Quick/Merge:**
- Quick Sort: no estable + O(n²) peor caso. Doble descarte.
- Merge Sort: estable y O(n log n). Funciona, pero Counting Sort es más
  rápido aprovechando que k=10.

---

## ✅ Caso 10: Strings largos — **Merge Sort**

**Análisis del problema:**
100,000 strings con potencial pre-orden por categoría. Necesitamos algo
estable, predecible y que aproveche el pre-orden si existe.

**¿Por qué Merge Sort?**
- O(n log n) garantizado: 100,000 × 17 ≈ 1.7M comparaciones (cada comparación
  de strings cuesta hasta 50 caracteres → 85M comparaciones de char).
- ✅ Es **estable** → mantiene el orden previo por categoría dentro de
  empates.
- Memoria disponible, así que el O(n) extra no es problema.
- Sin peor caso malo.

**¿Por qué NO los algoritmos no comparativos?**
- **Counting Sort**: solo para enteros, no aplica directamente a strings.
- **Radix Sort para strings**: existe (lexicographic radix sort), pero con
  d=50 caracteres y k=256 (ASCII) o más (Unicode), su rendimiento de
  O(d × (n + k)) = O(50 × (100,000 + 256)) ≈ 5 millones de operaciones puede
  ser comparable o peor que Merge Sort en la práctica, sobre todo por las
  constantes ocultas.
- **Bucket Sort**: requeriría definir cubetas por la primera letra y luego
  ordenar dentro. Funciona pero la distribución de letras NO es uniforme en
  español (más palabras con "a", "c", "p" que con "x", "k", "w").

**¿Por qué NO Quick Sort?**
Doble problema:
1. Peor caso O(n²) cuando los datos vienen casi ordenados → es exactamente lo
   que ocurre aquí (los productos vienen ordenados por categoría).
2. No es estable.

**¿Y Heap Sort?**
Funciona y garantiza O(n log n). El único problema es que **NO es estable**,
así que se pierde el pre-orden por categoría. Si la estabilidad no fuera
importante, Heap Sort es una opción válida con menor uso de memoria.

---

# 📊 Reglas heurísticas rápidas

| Si el caso menciona... | Probablemente uses... |
|------------------------|------------------------|
| Enteros con rango pequeño (k pequeño respecto a n) | **Counting Sort** |
| Enteros con muchos dígitos (k grande, d pequeño) | **Radix Sort** |
| Distribución uniforme conocida | **Bucket Sort** |
| Memoria muy limitada / sistemas embebidos | **Heap Sort** |
| Estabilidad requerida + memoria disponible | **Merge Sort** |
| Rendimiento promedio óptimo y datos aleatorios | **Quick Sort** |
| Garantía de peor caso obligatoria | NO uses Quick Sort |
| Datos casi ordenados | NO uses Quick Sort básico |
| Strings sin estructura aprovechable | Merge Sort o Heap Sort |
| Cola de prioridad DINÁMICA (insertar/extraer) | Heap (estructura) |
| Ordenar BATCH con prioridades pequeñas | Counting Sort (no Heap) |

---

# 🧠 Estrategia para responder estos casos

Cuando enfrentes un caso similar, sigue estos pasos:

1. **¿Los datos son enteros?**
   - Sí, y k pequeño → Counting Sort
   - Sí, y k grande pero d pequeño → Radix Sort
   - Sí, y distribución uniforme → Bucket Sort
   - No (reales/strings) → continúa al paso 2

2. **¿Hay restricción de memoria?**
   - Sí, severa → Heap Sort (O(1) extra)
   - No → continúa al paso 3

3. **¿Se requiere estabilidad?**
   - Sí → Merge Sort
   - No → continúa al paso 4

4. **¿Se acepta el peor caso O(n²)?**
   - Sí (datos aleatorios y rendimiento promedio importa) → Quick Sort
   - No (producción, datos potencialmente patológicos) → Heap Sort o Merge Sort

5. **Verifica casos extremos:**
   - ¿Hay pre-orden? → evita Quick Sort
   - ¿Datos repetidos masivos? → Counting Sort si son enteros
