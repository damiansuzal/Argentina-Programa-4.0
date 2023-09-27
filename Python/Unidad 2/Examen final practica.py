def cargar_empleado(datos):
    while True:
        try:
            nro_empleado = int(input("Ingrese el número de empleado: "))
            if nro_empleado <= 0: # si el numero es negativo
                print("El número de empleado debe ser positivo. Intente nuevamente.")
                continue # vuelve al while sin pasar a la siguiente linea
            
            nombre = str(input("Ingrese el nombre del empleado: "))
            edad = int(input("Ingrese la edad del empleado: "))
            sueldo = float(input("Ingrese el sueldo del empleado: "))
            
            datos[nro_empleado] = [nombre, edad, sueldo]
            print("Empleado cargado exitosamente.")
            break
        except ValueError: # si hay un error no para el programa y muestra este mensaje
            print("Valor incorrecto. Por favor, ingrese datos válidos.")

def calculo_empleado(datos, edad_limite):
    cantidad = 0
    for empleado in datos.values(): # el for recorre los elementos del diccionario datos
        if empleado[1] > edad_limite: # si el empleado tiene la edad mayor a la limite cuenta +1
            cantidad += 1
    print(f"Hay {cantidad} empleados con edad mayor a {edad_limite}.")

def busqueda_mayor(datos):
    maximo_sueldo= 0
    nro_empleado= -1
    for nro, empleado in datos.items(): # el for busca el numero y el empleado
        if empleado[2] >= maximo_sueldo: # compara el sueldo del empleado actual contra el mayor sueldo
            maximo_sueldo = empleado[2]
            nro_empleado = nro
            
    if nro_empleado >= 1: # si encontro al menos 1
        print(f"El empleado con mayor sueldo es #:{nro_empleado} con un sueldo de ${maximo_sueldo}")
    else:
        print("No hay empleados registrados")

def listado_registros(datos): 
    for nro_empleado, empleado in datos.items(): # busca los empleados e imprime sus datos
        print(f"Nro: {nro_empleado}, Nombre: {empleado[0]}, Edad: {empleado[1]}, Sueldo: {empleado[2]}")
    
def menu():
    
    datos = {} # declaro el diccionario vacio
    while True:
        print("\n--- Bienvenidos al Evil Corp Bank ---")
        print("1. Carga de valores del empleado ")
        print("2. Cálculo de cantidad de empleados con edad mayor a X")
        print("3. Búsqueda del mayor sueldo")
        print("4. Listado de los registros almacenados en el diccionario")
        print("S. Salir")
        opcion = input("Ingrese una opción: ")
        if opcion == "1":
            cargar_empleado(datos)
        elif opcion == "2":
            edad_limite = int(input("Ingrese la edad limite: "))
            calculo_empleado(datos, edad_limite)
        elif opcion == "3":
            busqueda_mayor(datos)
        elif opcion == "4":
            listado_registros(datos)
        elif opcion.lower() == "s":
            break
        else:
            print("Opción inválida. Intente nuevamente.")
menu()