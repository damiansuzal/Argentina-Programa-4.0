# Cargar un Diccionario con el nombre de tres alumnos y las notas de tres parciales.
# Validar las notas al cargar [0,10] • Mostrar el nombre de cada alumno y SOLO la mayor nota de los tres parciales.
# Mostrar el nombre de cada alumno y el promedio de las tres notas de los tres parciales.
# Cargar desde el teclado dos listas con valores reales, lista1 y lista2. Luego incluir en un diccionario las listas como
# valores para las claves : 'UNO' y 'DOS'
alumnos={}
valido=False
for i in range(3):
    clave= str(input("Ingrese el nombre del alumno nº" + str(i+1) + ": "))

    while not valido:
        nota1= float(input("Ingrese 1ª nota del alumno " + clave + ": "))
        nota2= float(input("Ingrese 2ª nota del alumno " + clave + ": "))
        nota3= float(input("Ingrese 3ª nota del alumno " + clave + ": "))
        if 0 <= nota1 <= 10 and 0 <= nota2 <= 10 and 0 <= nota3 <= 10: # valida que la nota este entre 0 y 10
            valido= True
        else:
            print("Ingrese las 3 notas validas de 0 a 10")
    notas=[nota1,nota2,nota3]
    prom_nota=(nota1 + nota2 + nota3)/3
    max_nota = max(notas) # calcula el maximo de las 3 notas
    alumnos[clave]= {"Mayor":max_nota, "Promedio":prom_nota} # agrega el elemento notas y la mayor de ellas al diccionario

    valido=False # una vez que agrega el elemento vuelve a poner valido como falso para que funcione el proximo while
print() # linea vacia
for clave in alumnos:
    print(clave)
print() # linea vacia
for alumno, detalles in alumnos.items():
    print("Alumno: ", alumno)
    print("Mejor nota: ", detalles["Mayor"])
    print("Promedio de las 3 notas: ", detalles["Promedio"])

print() # linea vacia
lista1=[]
lista2=[]
n= int(input("Ingrese la cantidad de elementos que tendra la lista 1: ")) # ingresa la cantidad de elementos a agregar
for i in range(n):
    elemento= float(input("Ingrese el elemento para la lista 1: "))
    lista1.append(elemento) # carga la lista

n= int(input("Ingrese la cantidad de elementos que tendra la lista 2: ")) # ingresa la cantidad de elementos a agregar
for i in range(n):
    elemento= float(input("Ingrese el elemento para la lista 2: "))
    lista2.append(elemento) # carga la lista

diccionario={"UNO":lista1, "DOS":lista2}
print("Diccionario obtenido:", diccionario)

