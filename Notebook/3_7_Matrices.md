# Introducción a las matrices en NumPy

Hasta ahora, hemos trabajado con lo que podríamos llamar "arreglos" en Python usando listas, una funcionalidad nativa del lenguaje. Pero hemos mencionado también que Python, en su forma estándar, no tiene un verdadero soporte para "arreglos" como lo conocemos en otros lenguajes de programación. Y sí, eso es cierto.

Pero aquí es donde NumPy entra en juego. NumPy es una biblioteca de Python que nos proporciona una estructura de datos tipo arreglo, el `ndarray`, optimizada para cálculos numéricos eficientes. En este módulo, vamos a aprender cómo trabajar con estos "arreglos" utilizando NumPy. Esta habilidad es esencial para muchas áreas en ciencia de datos, aprendizaje automático y computación científica, ya que nos permitirá manejar y realizar operaciones con conjuntos de datos numéricos de manera eficiente.

# Creación de matrices en NumPy

Podemos crear matrices en NumPy de varias formas. Aquí hay algunos ejemplos:


```python
import numpy as np

# Crear una matriz a partir de una lista de listas
A = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
print("A =\n", A)

# Crear una matriz de ceros
B = np.zeros((3, 3))
print("\nB =\n", B)

# Crear una matriz de unos
C = np.ones((3, 3))
print("\nC =\n", C)

# Crear una matriz con valores aleatorios
D = np.random.rand(3, 3)
print("\nD =\n", D)
```

Seguramente habrás notado en algún desafío anterior el uso de as en líneas de código como import libreria as lib. as en Python se utiliza para crear un alias durante la importación de un módulo. En este caso, estamos importando el módulo numpy y asignándole el alias np. Esto se hace por conveniencia para hacer el código más legible y conciso.

Después de esto, puedes usar el prefijo np. en lugar de numpy. para llamar a las funciones y métodos del módulo numpy. Esto es especialmente útil para módulos con nombres largos o que se utilizan con frecuencia.

El alias np para numpy es una convención ampliamente adoptada por la comunidad de Python, especialmente entre los científicos de datos, ingenieros y desarrolladores que utilizan numpy para el cálculo numérico. Utilizar estas convenciones ayuda a mantener el código coherente y fácil de leer entre diferentes proyectos y equipos. Sin embargo, podrías elegir cualquier nombre que desees para el alias. Por ejemplo, import numpy as nump también sería válido, pero no es comúnmente utilizado.

_Nota_: Puede ocurrir que Python no tenga NumPy en tu instalacion, lo resuelves con pip install numpy o similar según tu sistema.

# Acceso y modificación de elementos de la matriz

Podemos acceder y modificar elementos de la matriz utilizando índices. Veamos algunos ejemplos:


```python
# Acceder a un elemento
print("A[0, 0] =", A[0, 0])

# Modificar un elemento
A[0, 0] = 10
print("\nA =\n", A)
```

# Operaciones básicas con matrices

NumPy nos permite realizar varias operaciones con matrices, como suma, resta, producto escalar, producto de matrices y división. Veamos cómo hacerlo:


```python
# Crear dos matrices para las operaciones
A = np.array([[1, 2], [3, 4]])
B = np.array([[5, 6], [7, 8]])

# Suma de matrices
print("A + B =\n", A + B)

# Resta de matrices
print("\nA - B =\n", A - B)

# Producto escalar
print("\n2 * A =\n", 2 * A)

# Producto de matrices
print("\nA @ B =\n", A @ B)

# División de matrices
print("\nA / B =\n", A / B)
```

# Algunas operaciones especiales con matrices

Además de las operaciones básicas, NumPy también nos permite realizar algunas operaciones especiales con matrices, como transposición, determinante, inversa, traza y rango. Veamos cómo hacerlo:


```python
# Transposición de una matriz
print("A.T =\n", A.T)

# Determinante de una matriz
print("\nnp.linalg.det(A) =", np.linalg.det(A))

# Inversa de una matriz
print("\nnp.linalg.inv(A) =\n", np.linalg.inv(A))

# Traza de una matriz
print("\nnp.trace(A) =", np.trace(A))

# Rango de una matriz
print("\nnp.linalg.matrix_rank(A) =", np.linalg.matrix_rank(A))
```

# Desafío 1

Considere las matrices $ A $ y $ B $ definidas como:

$ A = \begin{bmatrix} 1 & 2 \\ 3 & 4 \end{bmatrix} $     y     $ B = \begin{bmatrix} 5 & 6 \\ 7 & 8 \end{bmatrix} $

Tu tarea es calcular la matriz resultante de la operación $ (2A + B^T) $. Recuerda que $ B^T $ denota la transposición de la matriz $ B $.

# Desafío 2

Dada la matriz $ A = \begin{bmatrix} 1 & 0 & 1 \\ 4 & -1 & 4 \\ 5 & 6 & 7 \end{bmatrix} $, encuentra la traza de la matriz inversa de $ A $.

# Desafío 3

Dada la matriz $ A = \begin{bmatrix} 1 & 2 & 3 \\ 4 & 5 & 6 \\ 7 & 8 & 9 \end{bmatrix} $, encuentra el rango de la matriz resultante de $ (A + A^T) $.

# Desafío 4: Batalla Naval

Para este desafío, tendrás que implementar un juego sencillo de "Batalla Naval". El tablero de juego será una matriz de 5x5 donde el agua será representada por ceros (0) y los barcos por unos (1).

Primero, crea un tablero de juego utilizando NumPy, que será una matriz de ceros de 5x5.

Luego, coloca tres barcos en el tablero de juego. Cada barco es un 1 y debes colocarlo en una posición aleatoria en el tablero. No te preocupes por el tamaño de los barcos; cada barco ocupará solo una celda.

Finalmente, crea una función que acepte dos argumentos (las coordenadas x, y), y que verifique si en esa posición hay un barco (1) o agua (0). La función debe imprimir un mensaje indicando si se golpeó un barco o si el disparo cayó al agua.

# Desafío 5: Crear una simulación de "vida artificial" en un tablero de juego (matriz)
En este desafío, implementarás una simulación del famoso Juego de la vida de Conway. Se trata de un autómata celular desarrollado por el matemático británico John Horton Conway en 1970. Es un juego de cero jugadores, lo que significa que su evolución se determina por su estado inicial, sin necesidad de más entradas humanas.

### Objetivos del Desafío
Crear el Tablero de Juego:

Implementa una función para crear un tablero de juego de dimensiones n x m, donde cada celda puede estar viva (1) o muerta (0). Inicializa el tablero con un patrón inicial.

### Definir las Reglas del Juego:

Cada celda en el tablero tiene 8 vecinos. Las reglas para la evolución del estado de las celdas son:
Una celda viva con menos de dos celdas vecinas vivas muere por subpoblación.
Una celda viva con dos o tres celdas vecinas vivas sigue viva en la siguiente generación.
Una celda viva con más de tres celdas vecinas vivas muere por sobrepoblación.
Una celda muerta con exactamente tres celdas vecinas vivas se convierte en una celda viva por reproducción.

### Simular la Evolución:

Implementa una función para actualizar el tablero siguiendo las reglas del juego. Esta función debería generar la nueva configuración del tablero después de un número específico de iteraciones.

### Visualizar la Simulación:

Utiliza Matplotlib para visualizar la evolución del tablero a lo largo de las iteraciones. Muestra cada estado del tablero como una imagen en una animación.
