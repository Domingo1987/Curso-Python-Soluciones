"""
DESAFIO 59: 
Diseña una clase LibroDigital que herede de Libro y añada 
atributos como formato (e.g., PDF, EPUB) y tamaño_archivo. 
Además, implementa una subclase EBook que sobrescriba un método 
para mostrar información específica, como enlaces de descarga.
"""

# SOLUCION

class Libro:
    def __init__(self, titulo, autor):
        self.titulo = titulo
        self.autor = autor

class LibroDigital(Libro):
    def __init__(self, titulo, autor, formato, tamanio_archivo):
        super().__init__(titulo, autor)
        self.__formato = formato
        self.__tamanio_archivo = tamanio_archivo
        
    def mostrar_info(self):
        return f"Formato: {self.__formato}, Tamaño: {self.__tamanio_archivo} MB"

class EBook(LibroDigital):
    def __init__(self, titulo, autor, formato, tamanio_archivo, enlace):
        super().__init__(titulo, autor, formato, tamanio_archivo)
        self.__enlace = enlace
        
    def mostrar_info(self):
        info_base = super().mostrar_info()
        return f"{info_base}, Enlace de descarga: {self.__enlace}"