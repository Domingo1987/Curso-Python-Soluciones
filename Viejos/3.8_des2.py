def capitalize_first_letters(text):
    """Capitaliza la primera letra de cada palabra en una cadena.
    
    Utiliza la función capitalize() para capitalizar la primera letra de una palabra.
    Documentación oficial de capitalize(): https://docs.python.org/3/library/stdtypes.html#str.capitalize
    
    Utiliza la función split() para dividir la cadena en palabras.
    Documentación oficial de split(): https://docs.python.org/3/library/stdtypes.html#str.split
    """
    lista_pal_separadas = text.split(' ',-1)
    lista_pal_mayus = []
    for pal in lista_pal_separadas:
        pal_mayus = pal.capitalize()
        lista_pal_mayus.append(pal_mayus)
    print(lista_pal_mayus)
    return ' '.join(lista_pal_mayus)

# Inicio la prueba
miTexto = "este texto es el texto de prueba"
miTexto = capitalize_first_letters(miTexto)
miTexto