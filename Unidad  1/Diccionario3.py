# Definir un diccionario y luego cargar N elementos. N se ingresa por teclado. Luego: •
# Recorrer el diccionario mostrando el par clave-valor • Devolver el número de elementos del diccionario •
# Recorrer el diccionario mostrando las claves • Insertar un nuevo elemento en el diccionario •
# Copiar un diccionario a otro vacío • Eliminar el diccionario original
dicc={}
n= int(input("Ingrese la cantidad de elementos a cargar: ")) # pide la cantidad de elementos a agregar
for i in range(n): # pide la cantidad de n veces, la clave y el valor del elemento actual
    clave= input("Ingrese la clave del elemento nº" + str(i+1) + ": ")
    valor= input("Ingrese el valor del elemento nº" + str(i+1) + ": ")
    dicc[clave]= valor # agrega el elemento al diccionario
print(dicc)
print() # linea vacia
print("El diccionario tiene", len(dicc), "elementos")
print() # linea vacia
for clave in dicc: # muestra solo las claves
    print(clave)
print() # linea vacia
dicc["clavenueva"]= n + 1
dicc_copia= dicc.copy() # copia un diccionario a otro
print("Diccionario dicc:" ,dicc)
print("Diccionario dicc_copia:" ,dicc_copia)
del dicc # elimina el diccionario
print("El Diccionario dicc ah sido eliminado:")
