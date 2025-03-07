def contar_platanos(platanos, total=0):
    if platanos == 0:
        return total  # Caso base: si no hay más plátanos, devolvemos el total acumulado
    else:
        print(f"El mono está contando un plátano... Total hasta ahora: {total + 1}")
        return contar_platanos(platanos - 1, total + 1)  # El mono cuenta un plátano más y sigue

# Prueba de la función
print(contar_platanos(5))  # El mono debería contar 5 plátanos, uno por uno.
