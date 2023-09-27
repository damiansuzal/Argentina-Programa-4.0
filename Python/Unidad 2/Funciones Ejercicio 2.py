#Idem al ejercicio anterior pero el carácter debe ser ingresado por teclado.
def recta(ancho, alto, simbol):
    for i in range (ancho): #Pone un simbolo en toda la linea
        print(simbol," ", end="")
    print()

    for i in range (alto-2):
        print(simbol," ", end="") #Pone un simbolo en la primera columna
        for j in range(ancho - 2): #Pone espacios vacios en el interior del rectangulo menos en las puntas
            print("   ", end="")
        print(simbol," ") #Pone un simbolo en la ultima columna

    for i in range(ancho):
        print(simbol," ", end="") #Pone un simbolo en la ultima linea

an= int(input ("Ingrese el ancho del rectangulo: "))
al= int(input ("Ingrese el alto del rectangulo: "))
simbolo= input("Ingrese un simbolo para formar un rectangulo: ")

recta(an, al, simbolo) #Llama a la funcion
