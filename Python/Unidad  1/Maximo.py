#Implementar un código que, ingresando 20 números, encuentre y devuelva el mayor de ellos.
for i in range(5):
    num = int(input("Ingrese un numero :"))
    if (i == 0):
        max=num
    elif (num > max):
        max=num
print("El numero maximo es: ", max)

