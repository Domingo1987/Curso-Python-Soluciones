"""
DESAFIO 62: 
Crea una clase Musico que tenga un método instrumento y crea dos subclases
Guitarrista y Baterista que sobrescriban el método instrumento. 
Instancia objetos de estas clases y demuestra el polimorfismo.
"""

# SOLUCION

from abc import ABC, abstractmethod

class Musico(ABC):
    def __init__(self, nombre):
        self.__nombre = nombre
    
    @property
    def nombre(self):
        return self.__nombre  
    
    @nombre.setter
    def nombre(self, nombre):
        self.__nombre = nombre  
    
    @abstractmethod
    def instrumento(self):
        pass
    
class Guitarrista(Musico):
    def __init__(self, nombre, marca):
        self.__marca = marca
        super().__init__(nombre)
        
    @property
    def marca(self):
        return self.__marca
    
    @marca.setter
    def marca(self, marca):
        self.__marca = marca
        
    def instrumento(self):
        return f"Strum strum strum {self.nombre}: Toca la guitarra {self.marca}"

class Baterista(Musico):
    def __init__(self, nombre, platillos):
        self.__platillos = platillos
        super().__init__(nombre)
        
    @property
    def platillos(self):
        return self.__platillos
    
    @platillos.setter
    def platillos(self, platillos):
        self.__platillos = platillos
    
    def instrumento(self):
        return f"Boom boom boom {self.nombre}: Toca la bateria de {self.platillos} platillos"

if __name__ == "__main__":    
    musico1 = Guitarrista("Saul", "Gibson")
    musico2 = Baterista("Juan", 5)

    print(musico1.instrumento())
    print(musico2.instrumento())
