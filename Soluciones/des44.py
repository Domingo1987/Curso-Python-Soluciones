"""
DESAFIO 44: Sistemas con Múltiples Entidades Interconectadas
Imagina un sistema de gestión de biblioteca que maneja libros, usuarios, préstamos 
y multas. Crear los TADs necesarios que contemple la gestión del contexto anterior.
"""

# SOLUCION
libros = []

def agregarLibro (libro):
    libros.append(libro)

def eliminarLibro (libro):
    libros.remove(libro)

def buscarLibro(idLibro):
    for libro in libros:
        if libro[0] == idLibro:
            return libro
    return None

usuarios = []

def agregarUsuario (usuario):
    pass

def eliminarUsuario (usuario):
    pass

def buscarUsuario (idUsuario):
    pass

prestamos = {}

def agregarPrestamo (idUsuario, idLibro):
    pass

def eliminarPrestamo (idLibro):
    pass

def buscarPrestamo (idLibro):
    pass

def buscarPrestamo (idUsuario):
    pass

multas = []

def agregarMulta (idUsuario, idMulta, multa):
    pass

def eliminarMulta (idUsuario, idMulta):
    pass

def buscarMulta (idUsuario, idMulta):
    pass

# Test

elLibro = (1, "El principito")
leLibro = (2, "El rey")
agregarLibro (elLibro)
agregarLibro (leLibro)

print("La cantidad de libros es: ", len(libros))
print("El libro numero ", buscarLibro(2)[0] ," es: ", buscarLibro(2)[1])