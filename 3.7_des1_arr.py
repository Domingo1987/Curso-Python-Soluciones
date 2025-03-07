# @title Solución
#Realizar el manejo del stock correspondiente a la verduleria y fruteria anadiendo productos, verificando stock.abs
inventario = ["manzanas", "bananas", "zanahorias", "espinacas", "brocoli", "cebolla","kiwis"]
#Pregunta 1: ¿Cuántos tipos de productos hay en el inventario inicial?
cont_inventario = len(inventario)
print(f"La cantidad de productos del inventario inicial es {cont_inventario}")

#Pregunta 2: ¿Qué producto está en la tercera posición del inventario?
tercer_producto = inventario[2]
print(f"El tercer producto es {tercer_producto}")

#Un cliente viene y compra todas las bananas.
#Pregunta 3: ¿Cómo actualizarías el inventario después de la venta?
inventario.remove("bananas")
print(inventario)

#Ahora recibes un envío de nuevos productos: "frutillas", "apio" y "papas".
#Pregunta 4:¿Cómo añadirias los productos al inventario?
#inventario.append("frutillas")
#inventario.append("apio")
#inventario.append("papas")
inventario.extend(["frutillas", "apio", "papas"])
print(inventario)

#Pregunta 5: ¿Cómo verificarias si las "papas"están ahora en el inventario?
if "papas" in inventario:
  print("Hay papas en el inventario\n")
else:
  print("No hay papas en el inventario")

#Pregunta 6:¿Cómo decidirías qué producto sacar para hacer espacio para el "dragonfruit"?
inventario.pop(0)
inventario.pop(0)
inventario.pop(0)
inventario.append("dragonfruit")
print(inventario)

#Pregunta 7:¿Cómo ordenarías el inventario?
inventario.sort()
print(f"El inventario ordenado queda de la siguiente manera: {inventario}\n")

#Pregunta 8:¿Cómo proporcionarías una copia del inventario al nuevo empleado, asegurándote de que si el empleado hace cambios en su copia, el inventario original no se vea afectado?
copia_inventario = inventario.copy()
copia_inventario.append("mandarinas")
print(f"Copia inventario {copia_inventario}\n")
print(f"inventario original {inventario}")