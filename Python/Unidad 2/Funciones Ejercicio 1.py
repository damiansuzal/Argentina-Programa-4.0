#Escriba un programa que por medio de una función pida la anchura y altura de un rectángulo y lo dibuje con caracteres producto (*).
def recta(ancho, alto):
    for i in range (ancho): #Pone * en toda la linea
        print("* ", end="")
    print()

    for i in range (alto-2):
        print("* ", end="") #Pone * en la primera columna
        for j in range(ancho - 2): #Pone espacios vacios en el interior del rectangulo menos en las puntas
            print("  ", end="")
        print("*") #Pone * en la ultima columna

    for i in range(ancho):
        print("* ", end="") #Pone * en la ultima linea

an= int(input ("Ingrese el ancho del rectangulo: "))
al= int(input ("Ingrese el alto del rectangulo: "))

recta(an, al) #Llama a la funcion
