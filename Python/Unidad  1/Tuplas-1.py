# Definir una tupla llamada “letras” con las primeras 6 letras del abecedario (en minúscula) por separado, es decir,
# cada letra es un elemento . Luego:
# Mostrar todos los elementos
# Mostrar todos los elementos del 2do al ultimo
# Mostrar todos los elementos del 1ro al 4to
# Mostrar todos los elementos del 3ro al 5to
# “Modificar” la tupla y cambiar las letras de minúsculas a mayúsculas
# Comprobar si existe en la tupla la letra con la que comienza tu nombre
# Determinar la cantidad de elementos de la tupla con la función len()
# Definir otra tupla “letras2” con las próximas 3 letras (en minúsculas)
# Unir “letras” y “letras2” en una sola tupla llamada “letras3”
# Mostrar las 3 tuplas por pantalla
letras = ("a","b","c","d","e","f")
print(letras)
print(letras[1:])
print(letras[:4])
print(letras[2:5])
nombre= input("Ingrese su nombre: ")
if nombre[0] in letras:
    print("Tu letra esta en la tupla")
else:
    print("Tu letra no esta en la tupla")
print(len(letras))
letras2 = ("g","h","i")
letras3 = letras + letras2
print("Tupla 1:",letras)
print("Tupla 2:",letras2)
print("Tupla 3:",letras3)
