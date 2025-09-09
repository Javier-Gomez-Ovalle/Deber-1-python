# 🃏 Mazo de Cartas en Python

Este proyecto implementa un **mazo de cartas barajado** y un **algoritmo de ordenamiento** en Python.  
El ejercicio demuestra cómo generar, mezclar y ordenar un mazo de cartas usando la técnica de **insertion sort**.

---

## 📂 Estructura del Proyecto

- **`barajar_mazo()`** → Genera un mazo de cartas con 52 combinaciones (13 valores × 4 palos) y lo baraja aleatoriamente.  
- **`insertion_sort(lista)`** → Implementación del algoritmo de ordenamiento por inserción.  
- **`main`** → Crea el mazo, lo imprime desordenado y luego muestra el resultado ordenado.  

---

## ⚙️ Instalación

Clona este repositorio:

```bash
git clone https://github.com/Javier-Gomez-Ovalle/Deber-1-python.git
cd mazo-cartas-python

```
Ejecuta el script con Python 3:

```
Copiar código
python mazo.py

```

▶️ Ejemplo de Ejecución

```
Copiar código
Mazo original: [(5, 'c'), (1, 't'), (12, 'p'), (7, 'd'), ...]
Mazo ordenado: [(1, 'c'), (2, 'c'), (3, 'c'), ..., (13, 'p')]
```
📌 También se puede mostrar con emojis de cartas para hacerlo más visual:

```bash
Copiar código
Mazo original: [7♦, 1♣, 12♥, 3♠, ...]
Mazo ordenado: [A♣, 2♣, 3♣, ..., K♠]
```
🧩 Explicación
Palos:

c → ♣ Tréboles

t → ♥ Corazones

d → ♦ Diamantes

p → ♠ Picas

Valores: 1 al 13 (pueden interpretarse como A = 1, J = 11, Q = 12, K = 13).

Algoritmo de ordenamiento:
Se usa insertion sort, un método sencillo y eficiente para listas pequeñas, que ordena comparando e insertando cada elemento en su posición correcta.

🌟 Posibles Mejoras
Representar las cartas con nombres (As, J, Q, K) en lugar de solo números.

Implementar otros algoritmos de ordenamiento (quicksort, mergesort) y comparar rendimiento.

Visualización del mazo en consola con símbolos de cartas (♥ ♦ ♣ ♠).

📜 Licencia
Este proyecto se distribuye bajo la licencia MIT.
