# Solución al Desafío 3 del cuaderno 3_7_Matrices
# Calcula el rango de la matriz resultante de A + A^T utilizando solo listas de Python

A = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

# Transposición de una matriz

def transpose(matrix):
    return [list(row) for row in zip(*matrix)]

# Suma de matrices

def add_matrices(M1, M2):
    return [
        [M1[i][j] + M2[i][j] for j in range(len(M1[0]))]
        for i in range(len(M1))
    ]

# Obtención de rango por reducción de filas (forma escalonada reducida)

def matrix_rank(matrix):
    m = len(matrix)
    n = len(matrix[0])
    M = [row[:] for row in matrix]  # copia para no modificar la original
    rank = 0
    for col in range(n):
        # encontrar pivote
        pivot_row = None
        for r in range(rank, m):
            if M[r][col] != 0:
                pivot_row = r
                break
        if pivot_row is None:
            continue
        # intercambiar filas
        M[rank], M[pivot_row] = M[pivot_row], M[rank]
        pivot = M[rank][col]
        # normalizar fila pivote
        M[rank] = [x / pivot for x in M[rank]]
        # eliminar la columna en otras filas
        for r in range(m):
            if r != rank:
                factor = M[r][col]
                if factor != 0:
                    M[r] = [M[r][c] - factor * M[rank][c] for c in range(n)]
        rank += 1
    return rank

At = transpose(A)
B = add_matrices(A, At)

rank_B = matrix_rank(B)

print("Rango de A + A^T:", rank_B)
