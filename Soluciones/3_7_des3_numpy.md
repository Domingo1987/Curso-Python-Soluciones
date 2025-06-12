# Desafío 3 - Rango de $A + A^T$ (versión NumPy)

El cuaderno `3_7_Matrices.md` plantea calcular el rango de la matriz
$A + A^T$ para
$$A = \begin{bmatrix} 1 & 2 & 3 \\ 4 & 5 & 6 \\ 7 & 8 & 9 \end{bmatrix}.$$

En esta segunda solución se utiliza la biblioteca **NumPy** para
simplificar el cálculo.

## 1. Crear la matriz en NumPy

```python
import numpy as np

A = np.array([
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
])
```

## 2. Calcular $A + A^T$

NumPy permite obtener la transpuesta con `A.T` y sumar matrices
con simples operaciones aritméticas:

```python
B = A + A.T
```

La matriz resultante es
$$\begin{bmatrix} 2 & 6 & 10 \\ 6 & 10 & 14 \\ 10 & 14 & 18 \end{bmatrix}.$$

## 3. Determinar el rango

Usamos `np.linalg.matrix_rank` para conocer el rango de `B`:

```python
rank_B = np.linalg.matrix_rank(B)
print("Rango de A + A^T:", rank_B)
```

La ejecución de `3_7_des3_numpy.py` muestra que el rango es 2.
