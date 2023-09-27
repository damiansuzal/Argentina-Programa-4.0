s= {'fruta':'Peras', 'cantidad': 10, 'precio': 35.10} # declara el diccionario
print("Fruta:", s["fruta"], ", Cantidad :", s["cantidad"]) # Muestra fruta y cantidad
print("El precio es:", s["precio"]) # muestra el precio solamente
s["precio"]= 75 # cambia el valor del precio
print("----------------") # linea vacia
print("El nuevo precio es:", s["precio"])
fecha= str(input("Ingrese la fecha de compra separada por guiones:"))
s["fecha"]= fecha # agrega un nuevo elemento al diccionario
print("----------------") # linea vacia
for clave in s: # muestra solo las claves
    print(clave)
print("----------------") # linea vacia
for clave,valor in s.items(): # muestra cada clave y valor del diccionario
    print(clave, valor)
print("----------------") # linea vacia
print(list(s)) # muestra el diccionario como lista
print("----------------") # linea vacia
del s["precio"] # elimina un elemento del diccionario
print(s)
