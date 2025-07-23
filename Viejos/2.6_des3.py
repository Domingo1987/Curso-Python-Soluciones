import random

def simular_carrera(nombres_autos, duracion=10):
  velocidades = {nombre: random.randint(5, 15) for nombre in nombres_autos} # Velocidad entre 5 y 15 m/s
  distancias = {nombre: 0 for nombre in nombres_autos}

  print("¡Comienza la carrera!")
  for segundo in range(1, duracion + 1):
    print(f"\n--- Segundo {segundo} ---")
    for nombre in nombres_autos:
      velocidad = velocidades[nombre]
      distancias[nombre] += velocidad
      print(f"{nombre} avanzó {velocidad} metros. Distancia total: {distancias[nombre]} metros.")

  # Determinar el ganador o los ganadores
  distancia_maxima = max(distancias.values())
  ganadores = [nombre for nombre, distancia in distancias.items() if distancia == distancia_maxima]

  print("\n--- ¡Carrera Terminada! ---")
  if len(ganadores) == 1:
    print(f"¡El ganador es {ganadores[0]} con una distancia de {distancia_maxima} metros!")
  else:
    print(f"¡Empate entre {', '.join(ganadores)} con una distancia de {distancia_maxima} metros!")

  return distancias

# Nombres de los autos participantes
autos = ["Rayo McQueen", "Chick Hicks", "Strip Weathers", "Meteoro"]

# Simular la carrera
resultados = simular_carrera(autos)