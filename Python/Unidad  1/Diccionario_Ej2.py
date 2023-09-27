"""Realizar un programa que permita la carga de datos de estudiantes. Los datos a cargar son: Nombre Completo, Nota 1 y Nota 2
Se debe mostrar el siguiente Menu:
1- Carga de estudiante
2- Mostrar la cantidad de estudiantes cargados
3- Mostrar el promedio de cada estudiante
4- Mostrar promedio mas alto
S- Salir"""
valido = False
alumnos = {}
calificaciones = []
menu = input("Bienvenidos al registro de usuarios, seleccione la opcion que desee: \n [1] Cargar alumno y notas \n [2] Mostrar la cantidad de estudiantes \n [3] Mostrar el promedio de cada estudiantes \n [4] Mostrar el promedio mas alto \n [S] Salir \n\n")
while menu.upper() != "S": # al no validar el input, hago que corte solo al presionar s o S

    if menu == "1": # si elijo la opcion 1 carga al estudiante y sus 2 notas
        nombre = str(input("Ingrese el nombre del alumno: "))
        nombre= nombre.upper()
        bandera= False
        for i in alumnos:
            if i==nombre:
                print("El estudiante ya se ha cargado.")
                bandera=True
        if bandera==False:
            nota1 = float(input("Ingrese 1ª nota del alumno " + nombre + ": "))
            nota2 = float(input("Ingrese 2ª nota del alumno " + nombre + ": "))
            if 0 <= nota1 <= 10 and 0 <= nota2 <= 10 : # valida que la nota este entre 0 y 10
                valido = True # cambio el valor de valido que es la variable bandera para salir del bucle
                print("Notas cargadas con exito")
                print() # linea vacia
            else:
                print("Ingrese las 2 notas validas de 0 a 10")
                print() # linea vacia
            notas = [nota1,nota2] # guardo las notas en la lista
            prom_nota = (nota1 + nota2)/len(notas) # calculo el promedio de las 3 notas podria usar--> sum(notas) / len(notas) si no supiera cuantas notas son
            max_nota = max(notas) # calcula el maximo de las notas
            calificaciones.append(notas) # carga la lista
        else:
            print("El nombre ya existe en el diccionario. Intente de nuevo.")
            bandera= True
            print() # linea vacia
        
        alumnos[nombre]= {"Notas":notas, "Mayor":max_nota, "Promedio":prom_nota} # agrega el elemento notas y la mayor de ellas al diccionario
        valido= False
        print() # linea vacia

    elif menu == "2": # si elijo la opcion 2 muestra la cantidad de estudiantes cargados
        print("La cantidad de estudiantes cargados es de", len(alumnos), "estudiantes")    
        print() # linea vacia                        

    elif menu == "3": # si elijo la opcion 3 muestra la a los estudiantes y sus promedios
        for alumno, detalles in alumnos.items():
            print("Alumno: ", alumno)
            print("Promedio de las 2 notas: ", detalles["Promedio"])
            print() # linea vacia
    
    elif menu == "4": # si elijo la opcion 4 muestra el promedio mas alto
            promedio_maximo=0
            for notas in alumnos.values():
                if notas["Promedio"]>promedio_maximo:
                    promedio_maximo =  notas["Promedio"]
            print("Promedio más alto:", promedio_maximo)
            print() # linea vacia

    else: # si presiono cualquier otra tecla que no sea 1,2,3,4,s o Ss
        print("Ingreso incorrecto, intente nuevamente")
        print()
    menu = input("Bienvenidos al registro de usuarios, seleccione la opcion que desee: \n [1] Cargar alumno y notas \n [2] Mostrar la cantidad de estudiantes \n [3] Mostrar el promedio de cada estudiantes \n [4] Mostrar el promedio mas alto \n [S] Salir \n\n")

print()
print("Terminando programa...")
print()

