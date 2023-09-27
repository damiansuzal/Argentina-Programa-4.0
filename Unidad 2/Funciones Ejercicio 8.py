"""Realiza una función separar(lista) que tome una lista de números enteros y devuelva dos listas ordenadas. 
La primera con los números pares y la segunda con los números impares."""
def separar_lista(lista):
    par= []
    impar = []
    for numero in lista:
        if numero % 2 == 0: #si es par
            par.append(numero) #almacena en pares
        else:
            impar.append(numero) #caso contrario en impares
    par.sort()
    impar.sort()
    return (par,impar)#retorna tupla de dos listas

lista_ejemplo = [7, 2, 4, 5, 8, 1, 3, 6]
pares, impares = separar_lista(lista_ejemplo)
print("Números pares:", pares)
print("Números impares:", impares)
