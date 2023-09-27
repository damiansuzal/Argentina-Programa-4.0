"""Crear una tupla con 10 valores.
Mostrar la suma de sus elementos y el promedio.
Además se pide averiguar si el cero esta o no dentro de la estructura"""
n= 10
lista= []
tupla= ()
suma= 0
numero= -1
for i in range(n):
    item= i+1
    numero = int(input(f"Ingrese el número {i+1}: "))
    lista.append(numero)
    suma += numero
    print()
tupla= tuple(lista)
print(tupla)
print()
if 0 in tupla:
    print("El 0 esta en la tupla")
else:
    print("El 0 no esta en la tupla")
print()
promedio= suma/len(tupla)
print(tupla)
print("El promedio de la suma es", promedio)