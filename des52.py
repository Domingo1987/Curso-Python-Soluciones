"""
DESAFIO 52: 
Crea una clase Libro que tenga atributos privados para el título, autor y ISBN. 
Proporciona métodos getter y setter para cada atributo.
"""

# SOLUCION

class Libro:
    def __init__(self, myTitulo, myAutor, myIsbn):
        self.__titulo = myTitulo
        self.__autor = myAutor
        self.__isbn = myIsbn

    # Métodos getter
    def getTitulo(self):
        return self.__titulo

    def getAutor(self):
        return self.__autor

    def getIsbn(self):
        return self.__isbn

    # Métodos setter
    def setTitulo(self, myTitulo):
        self.__titulo = myTitulo

    def setAutor(self, myAutor):
        self.__autor = myAutor

    def setIsbn(self, myIsbn):
        self.__isbn = myIsbn