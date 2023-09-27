"""Definir una función que calcule la longitud de una lista o una cadena dada. No utilizar la función len()."""
lista= ["Hola","Mundo","Como","Estas"] #lista ejemplo

cantidad= 0
def longitud():
    global cantidad #si no declaro la variable global dentro de la funcion tira error de variable no declarada
    for i in lista:
        cantidad = cantidad + 1
    return cantidad
    
largo= longitud()
print("La longitud de la lista es: ", largo)

    
