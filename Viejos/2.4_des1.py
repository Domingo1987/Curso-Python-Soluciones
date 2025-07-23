num1 = 7
num2 = 5
num3 = 7

# Inicializar variables para almacenar los números ordenados
minimo = medio = maximo = None

# Clasificar los números utilizando comparaciones encadenadas
if num1 < num2 <= num3 or num1 <= num3 <= num2:
    minimo = num1
elif num2 <= num1 <= num3 or num2 <= num3 <= num1:
    minimo = num2
else:
    minimo = num3

if num1 <= num2 <= num3 or num3 <= num2 <= num1:
    medio = num2
elif num2 <= num1 <= num3 or num3 <= num1 <= num2:
    medio = num1
else:
    medio = num3

#print(num1, ">=", num2, ">=", num3, " el valor es ", num1 >= num2 >= num3)
if num1 >= num2 >= num3 or num1 >= num3 >= num2:
    maximo = num1
elif num2 >= num1 >= num3 or num2 >= num3 >= num1:
    maximo = num2
else:
    maximo = num3

print("Números ordenados:", minimo, medio, maximo)