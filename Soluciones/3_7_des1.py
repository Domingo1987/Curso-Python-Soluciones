# Solución al Desafío 1 del cuaderno 3_7_Matrices
# Calcula la matriz (2A + B^T) utilizando solo listas de Python

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

for fila in resultado:
    print(fila)
