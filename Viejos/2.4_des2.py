# Defino las 5 variables para las calificaciones
nota1 = nota2 = nota3 = nota4 = nota5 = None
promedio = 0.0

nota1 = int(input("Ingrese la calificacion: "))
nota2 = int(input("Ingrese la calificacion: "))
nota3 = int(input("Ingrese la calificacion: "))
nota4 = int(input("Ingrese la calificacion: "))
nota5 = int(input("Ingrese la calificacion: "))

promedio = (nota1 + nota2 + nota3 + nota4 + nota5)/5

#Respondo el promedio de notas
print("Promedio es: ", promedio)