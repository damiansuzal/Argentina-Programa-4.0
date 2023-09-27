def cargar_producto(stock): #funcion que carga el producto
    clave = input("Ingrese el nombre del producto: ")

    peso = -1 
    while peso <= 0:
        peso = float(input("Ingrese el peso unitario del producto: "))
        if peso <= 0:
            print("El peso debe ser un valor numérico positivo.")
            print()

    cantidad = -1
    while cantidad <= 0:
        cantidad = int(input("Ingrese la cantidad del producto: "))
        if cantidad <= 0:
            print("La cantidad debe ser un valor entero positivo.")
            print()

    precio = -1
    while precio <= 0:
        precio = float(input("Ingrese el precio del producto: "))
        if precio <= 0:
            print("El precio debe ser un valor numérico positivo.")
            print()

    if clave in stock:
        print("El producto ya existe. Se actualizarán los valores.")
    stock[clave] = [peso, cantidad, precio]
    print("Producto cargado exitosamente.")
    print()


def vender_producto(stock, ventas): #funcion que vende un producto descontando el stock y sumando la compra
    nombre = input("Ingrese el nombre del producto a vender: ")
    if nombre in stock:
        cantidad_disponible = stock[nombre][1]
        cantidad_vender = -1
        while cantidad_vender <= 0 or cantidad_vender > cantidad_disponible:
            cantidad_vender = int(input("Ingrese la cantidad a vender: "))
            if cantidad_vender <= 0:
                print("La cantidad debe ser un valor entero positivo.")
                print()
            elif cantidad_vender > cantidad_disponible:
                print("No hay suficiente stock para realizar la venta.")
                print()

        total_venta = cantidad_vender * stock[nombre][2]
        stock[nombre][1] -= cantidad_vender
        ventas.append(total_venta)
        print("Venta realizada exitosamente. Total de la venta:", total_venta)
        print()
    else:
        print("El producto no existe.")
        print()


def listar_productos_con_stock_minimo(stock): #funcion que muestra los productos que tienen stock minimo
    n = -1
    while n <= 0:
        n = int(input("Ingrese el valor mínimo de stock: "))
        print()
        if n <= 0:
            print("El valor mínimo debe ser un número entero positivo.")
            print()

    productos_minimo_stock = []
    for clave, valores in stock.items(): #recorre el diccionario clave(producto) y valores(peso,cantidad,precio)
        if valores[1] < n: #si la cantidad es menor a n
            productos_minimo_stock.append(clave) #agrega a la lista el nombre del producto

    print("Productos con stock inferior a", n, ":") 
    print()
    if productos_minimo_stock:
        for producto in productos_minimo_stock:
            print(producto)
    else:
        print("No hay productos con stock inferior a", n)
        print()


def calcular_monto_total_ventas(ventas): #funcion que suma y muestra la cantidad de ventas
    if not ventas:
        print("No se han realizado ventas.")
        print()
    else:
        cantidad_ventas = len(ventas)
        monto_total = sum(ventas)
        print("Cantidad de ventas realizadas:", cantidad_ventas)
        print()
        print("Monto total de todas las ventas:", monto_total)
        print()


def eliminar_producto(stock): #funcion que elimina un producto
    nombre = input("Ingrese el nombre del producto a eliminar: ")
    print()
    if nombre in stock:
        del stock[nombre]
        print("Se eliminó el producto:", nombre)
        print()
    else:
        print("No existe el producto a eliminar.")
        print()


stock = {}
ventas = []
opcion= ""
while True :# al no validar el input, hago que corte solo al presionar f o F
    print("----------MENU PRINCIPAL----------")
    print("1) Cargar un producto")
    print("2) Vender un producto")
    print("3) Listar cantidad de productos con stock mínimo debajo de N")
    print("4) Calcular el monto total vendido en el día")
    print("5) Baja de un producto")
    print("f o F) Fin del programa")
    print()

    opcion = input("Seleccione una opción: ")
    print()

    if opcion == "1":
        cargar_producto(stock)
    elif opcion == "2":
        vender_producto(stock, ventas)
    elif opcion == "3":
        listar_productos_con_stock_minimo(stock)
    elif opcion == "4":
        calcular_monto_total_ventas(ventas)
    elif opcion == "5":
        eliminar_producto(stock)
    elif opcion.upper() == "F":
            break
    else:
        print("Opción inválida. Por favor, seleccione nuevamente.")
        print()