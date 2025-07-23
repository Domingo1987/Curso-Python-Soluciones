# main.py
import collections as col
import matplotlib.pyplot as plt




def analizadorDeTexto(textoParaAnalizar):
    if not textoParaAnalizar :
        print("El texto no es válido")
    else:
        #Counter es una subclase de dict que cuenta la frecuencia de los elementos. 
        #Almacena pares clave-valor donde la clave es el elemento de la colección 
        # y el valor es la cantidad de veces que ese elemento aparece
        #El método most_common(n) de un objeto Counter devuelve una lista de los n elementos más comunes 
        # y sus frecuencias en orden descendente
        
        palabrasMasComunes = col.Counter(textoParaAnalizar).most_common(10)  
        #llama a la función que genera la grafica y le pasa como parametro las palabras más usadas. 
        graficarDatos(palabrasMasComunes)
    

def graficarDatos(data):
    
    # Separa los datos en dos listas: palabras y frecuencias
    words, frequencies = zip(*data)

    # Crear la gráfica de barras con 10 pulgadas de ancho y 6 de alto 
    plt.figure(figsize=(10, 6))
    
    # words se utiliza para las etiquetas del eje X 
    # frequencies para la altura de las barras en el eje Y. 
    # El color de las barras se establece en 'skyblue'.
    plt.bar(words, frequencies, color='skyblue')

    # Añadir título y etiquetas
    plt.title('Frecuencia de palabras')
    plt.xlabel('Palabras')
    plt.ylabel('Frecuencia')

    # Mostrar la gráfica
    plt.show()
    
    
# Texto de ejemplo
texto = "Python es un lenguaje de alto nivel de programación interpretado cuya filosofía hace hincapié en la legibilidad de su código. Se trata de un lenguaje de programación multiparadigma, ya que soporta parcialmente la orientación a objetos, programación imperativa y, en menor medida, programación funcional."
# llamo a la función que analiza el texto 
print(analizadorDeTexto(texto.split(" ")))