# Realizar un programa que permita adivinar un número.
# Para ello se solicitara el ingreso por teclado del numero a adivinar (entero).
# Luego se irán solicitando mas números y se deberá ir averiguando si el número a adivinar es mayor o menor que el
# introducido (ir mostrando carteles indicativos). El programa termina cuando se acierta el número.
numero_para_adivinar = int(input("Ingrese un número a adivinar: "))
bandera=False
while bandera == False:
    numero_ingresado = int(input("Ingrese un número: "))

    if numero_ingresado == numero_para_adivinar:
        print("¡Felicitaciones! Has adivinado el número.")
        bandera= True
    elif numero_ingresado < numero_para_adivinar:
        print("El número a adivinar es mayor.")
    else:
        print("El número a adivinar es menor.")
