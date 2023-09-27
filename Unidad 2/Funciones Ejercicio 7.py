""""Escribir una función que reciba una frase y devuelva un diccionario con las palabras que contiene y su longitud."""
def contar_longitud_palabras(frase):
    # Dividir la frase en palabras
    palabras = frase.split()
    
    # Crear un diccionario para almacenar las palabras y sus longitudes
    diccionario_palabras = {}
    
    # Iterar sobre cada palabra y almacenar su longitud en el diccionario
    for palabra in palabras:
        diccionario_palabras[palabra] = len(palabra)
    
    return diccionario_palabras

# Ejemplo de uso
frase = input("Ingrese una frase: ")
resultado = contar_longitud_palabras(frase)
print(resultado)

