diccio= {1: "hola", 2: "cómo estás?", 3: "chau"}
lista_temporal= list(diccio)
print(lista_temporal)
print(type(lista_temporal))
lista_temporal.remove(2)
diccionario_modificado= tuple(lista_temporal)
print(diccionario_modificado)
print(lista_temporal)