"""
DESAFIO 47: 
Amplía la clase `Autor` para incluir una lista de libros escritos por el autor. Implementa métodos para agregar y eliminar libros de esta lista.
"""

# SOLUCION

class Autor:    
    # Defino el constructor
    def __init__(self, nombre, nacionalidad):
        self.nombre = nombre
        self.nacionalidad = nacionalidad
        self.libros = []
        
    # Metodo para verificar pertenencia de un libro
    def buscar_libro (self, libro):
        if libro in self.libros:
            return True
        return False
        
    # Método para agregar un libro
    def agregar_libro(self, libro):
        if not self.buscar_libro(libro):
            self.libros.append(libro)

    # Método para eliminar un libro
    def eliminar_libro(self, libro):
        if libro in self.libros:
            self.libros.remove(libro)
            
# main de prueba
if __name__=="__main__":
    miAutor = Autor("Carlos", "Uruguay")
    print(miAutor.nombre)
    print(miAutor.nacionalidad)
    
    # Agregamos un libro
    unLibro = "100 años de soledad"
    miAutor.agregar_libro(unLibro)
    
    print("Mostrar todos los libros: ", miAutor.libros)
    
    otroLibro = "100 años de soledades"
    miAutor.agregar_libro(otroLibro)
    
    print("Otra vez mostrar todos los libros: ", miAutor.libros)
    
            
    
