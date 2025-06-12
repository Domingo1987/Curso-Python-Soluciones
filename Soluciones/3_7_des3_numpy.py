import numpy as np

# Matriz original A
A = np.array([
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
])

# Calcular A + A^T de forma directa
B = A + A.T

# Obtener el rango de la matriz resultante
rank_B = np.linalg.matrix_rank(B)

print("Rango de A + A^T:", rank_B)
