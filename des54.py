"""
DESAFIO 54: 
Implementa la clase Autor con métodos getter y setter utilizando 
decoradores @property para manejar los atributos privados nombre 
y nacionalidad.
"""

# SOLUCION
class Autor:
    def __init__(self, myNombre, myNacionalidad):
        self.__nombre = myNombre
        self.__nacionalidad = myNacionalidad

    # Getter y Setter para nombre
    @property
    def nombre(self):
        return self.__nombre

    @nombre.setter
    def nombre(self, myNombre):
        self.__nombre = myNombre

    # Getter y Setter para nacionalidad
    @property
    def nacionalidad(self):
        return self.__nacionalidad

    @nacionalidad.setter
    def nacionalidad(self, myNacionalidad):
        self.__nacionalidad = myNacionalidad