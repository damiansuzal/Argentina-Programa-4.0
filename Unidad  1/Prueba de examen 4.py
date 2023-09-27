"""Crear un diccionario con N valores donde la clave sea el nombre del usuario y el valor sea el teléfono. 
N es una constante determinada por el usuario. No se podrán cargar nombres repetidos.
Mostrar el diccionario """
N = int(input("Ingrese la cantidad de valores para el diccionario: "))
agenda = {}
valido= False
while not valido:
    for i in range(N):
        nombre = input("Ingrese el nombre del usuario: ")
        nombre= nombre.upper()
        telefono = input("Ingrese el número de teléfono: ")
        if nombre not in agenda:
            agenda[nombre] = telefono
            valido= True
        else:
            print("El nombre ya existe en el diccionario. Intente de nuevo.")
            valido= False
print("\nAgenda:")
print("Nombre - Telefono")
for nombre, telefono in agenda.items():
    print(nombre + ": " + telefono)