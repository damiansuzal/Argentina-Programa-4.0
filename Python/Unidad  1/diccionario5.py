# Se quiere cargar los nombres y notas de tres parciales de los alumnos.
# Para ello se propone usar un diccionario que como clave tenga el nombre del alumno y como valores una
# lista para las notas de los parciales-. Crear un menú como el siguiente: 1) Cargar alumno y notas
# 2) Mostrar el nombre y promedio mas alto. S o S) Salir.- OBS. • No deben existir dos nombres iguales,
# hay que validar y solicitar reingreso si se da esa situación. • Las notas deben pertenecer a [0,10] si no es el caso
# solicitar reingreso. • Ver que no puedo ejecutar el punto 2 si al menos no ejecute el punto 1.
valido = False
alumnos = {}
calificaciones = []
menu = input("Bienvenidos al registro de usuarios, seleccione la opcion que desee: \n [1] Cargar alumno y notas \n [2] Mostrar el nombre y promedio \n [S] Salir \n\n")
while menu.upper() != "S": # al no validar el input, hago que corte solo al presionar s o S

    if menu == "1": # si elijo la opcion 1 hace esto
        clave = str(input("Ingrese el nombre del alumno: "))
        while not valido: # mientras valido sea false se ejecuta el bucle
            nota1 = float(input("Ingrese 1ª nota del alumno " + clave + ": "))
            nota2 = float(input("Ingrese 2ª nota del alumno " + clave + ": "))
            nota3 = float(input("Ingrese 3ª nota del alumno " + clave + ": "))
            if 0 <= nota1 <= 10 and 0 <= nota2 <= 10 and 0 <= nota3 <= 10: # valida que la nota este entre 0 y 10
                valido = True # cambio el valor de valido que es la variable bandera para salir del bucle
                print("Notas cargadas con exito")
                print()
            else:
                print("Ingrese las 3 notas validas de 0 a 10")
        notas = [nota1,nota2,nota3] # guardo las notas en la lista
        prom_nota = (nota1 + nota2 + nota3)/3 # calculo el promedio de las 3 notas podria usar--> sum(notas) / len(notas) si no supiera cuantas notas son
        max_nota = max(notas) # calcula el maximo de las 3 notas
        calificaciones.append(notas) # carga la lista
        alumnos[clave]= {"Notas":notas, "Mayor":max_nota, "Promedio":prom_nota} # agrega el elemento notas y la mayor de ellas al diccionario
        valido= False
        print()

    elif menu == "2": # si elijo la opcion 2 hace esto
        for alumno, detalles in alumnos.items():
            print("Alumno: ", alumno)
            print("Promedio de las 3 notas: ", detalles["Promedio"])
            print() # linea vacia

    else: # si presiono cualquier otra tecla que no sea 1,2,s o Ss
        print("Ingreso incorrecto, intente nuevamente")
        print()
    menu = input("Bienvenidos al registro de usuarios, seleccione la opcion que desee: \n [1] Cargar alumno y notas \n [2] Mostrar el nombre y promedio \n [S] Salir \n\n")
print()
print("Terminando programa...")
print()

