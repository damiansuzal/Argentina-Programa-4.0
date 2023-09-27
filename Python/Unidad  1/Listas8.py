# ¿Sabrías hacer que Python te diga cuántas repeticiones del valor 10 hay en esta lista?
lista_numeros = [10,45,356,10,10,10,46,67,45,10,10,43,10,65,10,10]
lista_sin_duplicados=[]
for numero in lista_numeros:
    if numero not in lista_sin_duplicados:
        lista_sin_duplicados.append(numero)
print(lista_sin_duplicados)
