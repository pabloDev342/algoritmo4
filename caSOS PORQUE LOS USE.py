## 🎯 CASO 1 — Universidad (Notas)

## 📌 Situación

Una universidad necesita ordenar las notas finales de 200 estudiantes.

Las notas:

* son enteros,
* van de 0 a 100,
* y si dos estudiantes tienen la misma nota,
  deben mantener el orden alfabético.

---

## ✅ Algoritmo usado: Counting Sort

## ✅ ¿Por qué usaría Counting Sort?

Usaría Counting Sort porque:

* las notas son enteros,
* el rango es pequeño,
* y necesitamos estabilidad.

Como solo existen 101 valores posibles, el algoritmo puede contar rápidamente cuántas veces aparece cada nota.

Además, Counting Sort es estable, así que si dos estudiantes tienen la misma nota, conserva el orden original.

### ✅ Complejidad

O(n+k)

---

# 🎯 CASO 2 — Banco (Transacciones)

## 📌 Situación

Un banco necesita ordenar 1 millón de transacciones.

El servidor:

* tiene poca memoria disponible,
* y necesita tiempos seguros en producción.

---

## ✅ Algoritmo usado: Heap Sort

## ✅ ¿Por qué usaría Heap Sort?

Usaría Heap Sort porque:

* consume muy poca memoria,
* funciona directamente sobre el arreglo,
* y garantiza buen rendimiento siempre.

En producción no podemos arriesgarnos a que el algoritmo se vuelva lento inesperadamente.

Heap Sort garantiza:

O(n\log n)

en todos los casos.

Además usa memoria:

O(1)

---

# 🎯 CASO 3 — Recursos Humanos

## 📌 Situación

Una empresa ya tiene empleados ordenados por salario.

Ahora necesita ordenarlos por departamento SIN perder el orden salarial.

---

## ✅ Algoritmo usado: Merge Sort

## ✅ ¿Por qué usaría Merge Sort?

Usaría Merge Sort porque el problema necesita estabilidad.

La estabilidad permite mantener el orden anterior cuando dos elementos pertenecen al mismo departamento.

Eso significa que el orden salarial no se pierde.

Merge Sort:

* es estable,
* seguro,
* y garantiza:

O(n\log n)

---

# 🎯 CASO 4 — Registraduría (Cédulas)

## 📌 Situación

La Registraduría necesita ordenar 10 millones de cédulas.

Las cédulas:

* tienen hasta 10 dígitos,
* y el rango es enorme.

---

## ✅ Algoritmo usado: Radix Sort

## ✅ ¿Por qué usaría Radix Sort?

Usaría Radix Sort porque:

* los datos son enteros,
* tienen muchos dígitos,
* y el rango es demasiado grande para Counting Sort.

Radix Sort ordena número por número usando cada dígito individualmente.

Eso permite ordenar enormes cantidades de datos muy rápido.

### ✅ Complejidad

O(d(n+k))

---

# 🎯 CASO 5 — Sensor IoT

## 📌 Situación

Un sensor industrial tiene solamente 4 KB de RAM.

Necesita ordenar temperaturas almacenadas.

---

## ✅ Algoritmo usado: Heap Sort

## ✅ ¿Por qué usaría Heap Sort?

Usaría Heap Sort porque:

* el dispositivo tiene muy poca memoria,
* y Heap Sort usa memoria mínima.

Además:

* trabaja directamente sobre el arreglo,
* y no necesita arreglos auxiliares.

Eso es muy importante en sistemas embebidos.

---

# 🎯 CASO 6 — Sensor ambiental

## 📌 Situación

Un sistema recibe 86,400 mediciones diarias entre 0 y 100.

---

## ✅ Algoritmo usado: Counting Sort

## ✅ ¿Por qué usaría Counting Sort?

Usaría Counting Sort porque:

* el rango es muy pequeño,
* hay muchísimos datos repetidos,
* y ordenar comparando sería innecesario.

Counting Sort puede ordenar prácticamente en tiempo lineal.

### ✅ Complejidad

O(n+k)

---

# 🎯 CASO 7 — Empresa logística

## 📌 Situación

Una empresa necesita ordenar paquetes por código postal.

Los datos están distribuidos uniformemente.

---

## ✅ Algoritmo usado: Bucket Sort

## ✅ ¿Por qué usaría Bucket Sort?

Usaría Bucket Sort porque fue diseñado para distribuciones uniformes.

El algoritmo divide los datos en cubetas.

Como los datos están bien distribuidos:

* cada cubeta tendrá pocos elementos,
* y el ordenamiento será muy rápido.

### ✅ Complejidad promedio

O(n+k)

---

# 🎯 CASO 8 — Cola de procesos

## 📌 Situación

Un sistema operativo necesita ordenar procesos por prioridad.

Las prioridades:

* van de 1 a 10,
* y debe mantenerse FIFO.

---

## ✅ Algoritmo usado: Counting Sort

## ✅ ¿Por qué usaría Counting Sort?

Usaría Counting Sort porque:

* el rango de prioridades es pequeño,
* y necesitamos estabilidad.

FIFO significa mantener el orden de llegada.

Counting Sort es estable y conserva ese orden automáticamente.

---

# 🎯 CASO 9 — Marketplace

## 📌 Situación

Una tienda online necesita ordenar productos por nombre.

Los nombres:

* son strings largos,
* y el sistema necesita estabilidad.

---

## ✅ Algoritmo usado: Merge Sort

## ✅ ¿Por qué usaría Merge Sort?

Usaría Merge Sort porque:

* garantiza rendimiento estable,
* no tiene peor caso peligroso,
* y conserva el orden previo.

Eso es ideal para catálogos grandes.

### ✅ Complejidad

O(n\log n)
