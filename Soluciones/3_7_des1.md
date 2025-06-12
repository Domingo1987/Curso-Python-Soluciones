# Desafío 1 - Operaciones con matrices

En el cuaderno `3_7_Matrices.md` se plantea el siguiente ejercicio:

> Considere las matrices $A$ y $B$ definidas como
>
> $A = \begin{bmatrix}1 & 2\\3 & 4\end{bmatrix}$ y
> $B = \begin{bmatrix}5 & 6\\7 & 8\end{bmatrix}$.
>
> Calcular la matriz resultante de la operación $2A + B^T$.

El archivo `desafio1.py` muestra una solución sencilla utilizando listas de Python para evitar dependencias externas:

```python
A = [[1, 2], [3, 4]]
B = [[5, 6], [7, 8]]

# Transpuesta de B
def transpose(matrix):
    return [list(row) for row in zip(*matrix)]

# Suma de matrices de igual tamaño
def add_matrices(M1, M2):
    return [[M1[i][j] + M2[i][j] for j in range(len(M1[0]))] for i in range(len(M1))]

# Multiplicación por escalar
def scalar_multiply(s, M):
    return [[s * elem for elem in row] for row in M]

Bt = transpose(B)
resultado = add_matrices(scalar_multiply(2, A), Bt)
print(resultado)
```

El resultado obtenido es:

```
[7, 11]
[12, 16]
```

Esta matriz corresponde a $2A + B^T$, donde $B^T$ es la transpuesta de $B$.
