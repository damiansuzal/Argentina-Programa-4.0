# Escriba un programa que permita que una función reciba una lista de valores (que puede ser vacía). 
# El programa tiene que pedir un número y luego solicitar ese número de valores para crear la lista. 
# Luego, a traves de otra función devolver al programa principal la lista y el mayor y menor valor de la misma
def carga_lista():
    lista= []
    n = int(input("Ingrese el tamaño de su lista: ")) #Pedimos al usuario el numero de elementos a ingresar en nuestra lista
    
    for i in range (n):
        valor = int(input("Ingrese el numero: "))
        lista.append(valor) #agrega los elementos al final de la lista
    return lista

def max_min(lista):
    minimo = min(lista)
    maximo = max(lista)
    return(minimo, maximo)

mi_lista= carga_lista()
(min, max) = max_min(mi_lista)
print ("La lista creada es", mi_lista)
print ("El valor minimo es:", min, "y el maximo es:", max)

