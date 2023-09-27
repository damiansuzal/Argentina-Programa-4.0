# Ingresar valores numéricos por teclado e ir guardándolos en una lista. El final del ingreso de números esta dado por el
# ingreso de un número negativo. Se pide luego:
# a) Mostrar los números pares de la lista (si no se ingreso ninguno, mostrar un cartel)
# b) El máximo valor de los números guardados en la lista.
numeros = []
num = 0
pares = []

while num >= 0:  # Agrega numeros a la lista hasta que se ingresa uno negativo
    num = int(input("Ingrese un numero positivo: "))
    numeros.append(num)
print("Ingreso un numero negativo, cerrando programa")

for numero in numeros:  # carga solo los numeros pares en una lista nueva
    if numero % 2 == 0:
        pares.append(numero)
print(pares)

maximo = pares[0]  # muestra el maximo numero de la lista pares
for numero in pares:
    if numero > maximo:
        maximo = numero
print("El valor maximo es: ", maximo)
