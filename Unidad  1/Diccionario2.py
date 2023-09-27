# Definir un diccionario con 4 elementos. Las claves son clave1, clave2, clave3 y clave4.
# Y los valores correspondientes a cada clave son: un valor entero, un valor booleano, un string y una lista que contiene
# los números desde el 1 al 4. a) Mostrar a que tipo corresponde la estructura completa. b) Mostrar cada uno de sus valores
# usando sus claves c) Mostrar que tipo de dato tiene cada valor de clave d) Agregar un elemento más al diccionario
# e) Ingresar por teclado un dato y determinar si existe una clave que coincida con alguna clave del diccionario.
# Si se encuentra mostrar el valor asociado f) Copiar en forma “superficial” el diccionario y modificar el primer valor de clave.
# Observar que sucede con el diccionario original Poner el valor cero a todos los valores del diccionario
# g)Recorrer y mostrar todos los elementos clave-valor del diccionario Ingresar por teclado un dato y eliminar del diccionario
# dicho dato si se encuentra dentro del diccionario. h)Eliminar todos los elementos del diccionario
dicc= {"clave1":1, "clave2":True, "clave3":"negro", "clave4":[1,2,3,4]}
print(type(dicc))
print() # linea vacia
for valor in dicc.values(): # muestra solo los valores
    print(valor)
    print(type(valor))
    print()
print() # linea vacia
dicc["clave5"]=3.14
print() # linea vacia
dato= input("Ingrese un dato a buscar en el diccionario: ") # pide un dato a buscar y lo almacena
print() # linea vacia
if dato in dicc.values(): # si el dato es encontrado va por el if
    print("El dato fue encontrado en el diccionario")
else:
    print("El dato no existe en el diccionario")
