import numpy as np

TAM = 5

# Crear un tablero de juego TAMxTAM
def crearTablero(i):
    tablero = np.zeros((i,i))
    return tablero


# Colocar tres(por ahora) barcos en posiciones aleatorias
def colocarBarcos(tab, cant):
    while cant != 0:
        x, y = np.random.randint(0, 5, size=2)
        if tab[x,y] == 0:
            tab[x,y] = 1
            cant -= 1
    return tab

# Función para verificar si hay un barco o agua en las coordenadas dadas
 

# Prueba la función con algunas coordenadas


# A JUGAR!!
miTablero = crearTablero(TAM)
print("Muestro el tablero sin Barcos")
print(miTablero)

colocarBarcos(miTablero, 3)
print("Muestro el tablero con Barcos")
print(miTablero)