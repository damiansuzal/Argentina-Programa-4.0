# Escribir un programa que pida al usuario una palabra y muestre por pantalla si es un palíndromo.
palabra= input("Ingrese una palabra: ")
palabra= palabra.lower() # convierte la palabra a miniscula
ordenada = list(palabra)
invertida= []

for i in range(len(ordenada)-1, -1, -1):
    invertida.append(ordenada[i])
if ordenada == invertida:
    print("La palabra es un palindromo")
else:
    print("La palabra no es un palindromo")
print(invertida)
