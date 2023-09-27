""" Si elige el punto 3 deberá mostrar la cantidad de operaciones D y E que se hicieron y el monto total de las mismas.
"""
clientes = {}  # Diccionario para almacenar los clientes
def cargar_cliente():
    numero_cliente = input("Ingrese el número de cliente: ")

    if numero_cliente in clientes:
        print("Cliente encontrado. Datos del cliente:")
        print("Número de cliente:", numero_cliente)
        print("Nombre:", clientes[numero_cliente]["nombre"])
        print("Saldo:", clientes[numero_cliente]["saldo"])
    else:
        agregar = input("Cliente no encontrado. ¿Desea agregarlo? (S/N): ")
        if agregar.lower() == "s":
            nombre = input("Ingrese el nombre del cliente: ")
            clientes[numero_cliente] = {"nombre": nombre, "saldo": 0}
            print("Cliente agregado con saldo inicial de 0.")
        else:
            print("Operación cancelada.")

def operacion():
    numero_cliente = input("Ingrese el número de cliente: ")

    if numero_cliente in clientes:
        codigo_operacion = input("Ingrese el código de operación (D: depósito, E: extracción): ")

        if codigo_operacion.upper() == "D":
            monto = float(input("Ingrese el monto a depositar: "))
            clientes[numero_cliente]["saldo"] += monto
            print(f"Depósito realizado. Saldo actual: {clientes[numero_cliente]['saldo']}")
        elif codigo_operacion.upper() == "E":
            monto = float(input("Ingrese el monto a extraer: "))
            if monto <= clientes[numero_cliente]["saldo"]:
                clientes[numero_cliente]["saldo"] -= monto
                print(f"Extracción realizada. Saldo actual: {clientes[numero_cliente]['saldo']}")
            else:
                print("No hay suficiente saldo para realizar la extracción.")
        else:
            print("Código de operación inválido. Debe ser D o E.")
    else:
        print("Número de cliente inexistente.")

def registro_operaciones(clientes):
    total_depositos = 0
    total_extracciones = 0
    monto_depositos = 0
    monto_extracciones = 0

    for cliente in clientes.values():
        total_depositos += cliente.get("depositos", 0)
        total_extracciones += cliente.get("extracciones", 0)
        monto_depositos += cliente.get("monto_depositos", 0)
        monto_extracciones += cliente.get("monto_extracciones", 0)

    print("\n--- Registro de operaciones ---")
    print("Cantidad de depósitos realizados:", total_depositos)
    print("Cantidad de extracciones realizadas:", total_extracciones)
    print("Monto total de depósitos:", monto_depositos)
    print("Monto total de extracciones:", monto_extracciones)

def menu():
    while True:
        print("\n--- Bienvenidos al Evil Corp Bank ---")
        print("1. Cargar cliente")
        print("2. Operación")
        print("3. Registro de operaciones")
        print("S. Salir")

        opcion = input("Ingrese una opción: ")

        if opcion == "1":
            cargar_cliente()
        elif opcion == "2":
            operacion()
        elif opcion == "3":
            registro_operaciones(clientes)
        elif opcion.lower() == "s":
            break
        else:
            print("Opción inválida. Intente nuevamente.")

menu()


    
