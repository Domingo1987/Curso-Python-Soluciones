"""
DESAFIO 60: 
Implementa una clase EscritorAcademico que herede de Escritor y 
Academico, e incluya un método adicional para publicar artículos 
académicos. Asegúrate de utilizar correctamente la función super()
para inicializar las clases base.
"""

# SOLUCION
class Escritor:
    def __init__(self, nombre, genero):
        self.nombre = nombre
        self.genero = genero

    def escribir(self, texto):
        return f"{self.nombre} está escribiendo: {texto}"
    
class Academico:
    def __init__(self, campo_estudio, institucion):
        self.campo_estudio = campo_estudio
        self.institucion = institucion

    def publicar_articulo(self, titulo):
        return f"Artículo '{titulo}' publicado en el campo de {self.campo_estudio} por {self.institucion}"

class EscritorAcademico(Escritor, Academico):
    def __init__(self, nombre, genero, campo_estudio, institucion):
        Escritor.__init__(self, nombre, genero)
        Academico.__init__(self, campo_estudio, institucion)

    def escribir_articulo(self, titulo, contenido):
        return f"{self.nombre} está escribiendo un artículo en {self.campo_estudio}: {titulo}\nContenido: {contenido}"  