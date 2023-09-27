#Pedir tres números por teclado e imprimir el mayor de ellos solamente.
for i in range(3):
    num = int(input("Ingrese un numero: "))
    if (i == 0):
        max=num
    elif (num > max):
        max=num
print("El numero maximo es: ", max)
