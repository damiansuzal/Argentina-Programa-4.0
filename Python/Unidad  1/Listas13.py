# Defina la siguiente lista: [1,4,4,5,9,4,6,4,8,7,3,4]. Escriba un código que cuente la cantidad de veces que se repite un número
# ingresado por teclado.
lista=[1,4,4,5,9,4,6,4,8,7,3,4]
contador=0
num=int(input("Ingrese un numero: "))
for numero in lista:
    if num == numero:
        contador= contador + 1
print("El numero",num, "se repite", contador,"veces.")
