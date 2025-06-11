# Desafío 2 - Traza de la inversa de una matriz

En el cuaderno `3_7_Matrices.md` se plantea el siguiente ejercicio:

> Dada la matriz $A = \begin{bmatrix} 1 & 0 & 1 \\ 4 & -1 & 4 \\ 5 & 6 & 7 \end{bmatrix}$,
> encuentra la traza de la matriz inversa de $A$.

El archivo `desafio2.py` implementa una solución empleando exclusivamente listas
de Python. Se calcula la inversa de $A$ mediante el método de la adjunta y luego
se obtiene su traza:

```python
A = [
    [1, 0, 1],
    [4, -1, 4],
    [5, 6, 7]
]

# ... funciones para determinante, cofactores e inversa ...

inv_A = inverse(A)
trace_inv = sum(inv_A[i][i] for i in range(len(A)))
print("Traza de A^{-1}:", trace_inv)
```

Al ejecutar el script se obtiene el siguiente resultado:

```
Traza de A^{-1}: 15.0
```

Por lo tanto, la traza de la matriz inversa de $A$ es 15.
