# Solución al Desafío 2 del cuaderno 3_7_Matrices
# Calcula la traza de la matriz inversa de A utilizando solo listas de Python

A = [
    [1, 0, 1],
    [4, -1, 4],
    [5, 6, 7]
]

# Submatriz que resulta de eliminar la fila i y la columna j

def minor(matrix, i, j):
    return [row[:j] + row[j+1:] for row in (matrix[:i] + matrix[i+1:])]

# Determinante de una matriz 2x2

def det2(m):
    return m[0][0] * m[1][1] - m[0][1] * m[1][0]

# Determinante recursivo (solo 2x2 o 3x3 en este contexto)

def determinant(m):
    if len(m) == 2:
        return det2(m)
    det = 0
    for j in range(len(m)):
        det += ((-1) ** j) * m[0][j] * determinant(minor(m, 0, j))
    return det

# Matriz de cofactores

def cofactor_matrix(m):
    n = len(m)
    cof = []
    for i in range(n):
        row = []
        for j in range(n):
            row.append(((-1) ** (i + j)) * determinant(minor(m, i, j)))
        cof.append(row)
    return cof

# Transposición de una matriz

def transpose(matrix):
    return [list(row) for row in zip(*matrix)]

# Divide todos los elementos de la matriz por un escalar

def divide_by_scalar(matrix, s):
    return [[elem / s for elem in row] for row in matrix]

# Inversa por el método de la adjunta

def inverse(m):
    det = determinant(m)
    cof = cofactor_matrix(m)
    adj = transpose(cof)
    return divide_by_scalar(adj, det)

inv_A = inverse(A)

# Calcular la traza
trace_inv = sum(inv_A[i][i] for i in range(len(A)))

print("Traza de A^{-1}:", trace_inv)
