def mcd (a,b):
    while b!=0:
        a, b = b, a % b
    return a

num1 = int(input("Ingrese un numero diferente de cero"))
num2 = int(input("Ingrese otro numero diferente de cero"))
res = mcd(num1,num2)
print(res)