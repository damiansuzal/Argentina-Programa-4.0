"""
Si elige 4, utiliza la lista que contiene los totales de cada venta y muestra la cantidad de ventas realizadas y total de todas las ventas.
Si elige 5, debe ingresar un nombre de producto y, si existe la clave elimina el producto y muestra un cartel: "Se eliminó el producto". 
Si no existe la clave se muestra un cartel "No existe el producto a eliminar"."""
productos={}
opcion= ""
valido= False
venta_diaria= []
while opcion.upper() != "F": # al no validar el input, hago que corte solo al presionar f o F
    print("----------MENU PRINCIPAL----------")
    print("1) Cargar un producto")
    print("2) Vender un producto")
    print("3) Listar cantidad de productos con stock mínimo debajo de N")
    print("4) Calcular el monto total vendido en el día")
    print("5) Baja de un producto")
    print("f o F) Fin del programa")
    print()
    opcion=input("Ingrese una opcion: ")
    print()
    if opcion == "1":
        producto= input("Ingrese el nombre del producto: ")
        producto= producto.upper()
        bandera= False
        for i in productos:
            if i==producto:
                print("El producto ya existe.")
                bandera=True
        if bandera==False:
            peso= float(input("Ingrese el peso del producto en gramos: "))
            cantidad= int(input("Ingrese la cantidad del producto: "))
            precio= float(input("Ingrese el precio del producto: "))
            productos[producto]=[peso,cantidad,precio]
            print("El producto se cargó correctamente")
            print()
    if opcion == "2":
        producto= input("Ingrese el nombre del producto a vender: ")
        producto= producto.upper()
        bandera= False
        valido= False
        for i in productos:
            if producto == i:
                valido= True
            if not valido:
                print("El producto ingresado no existe")
            else:
                cantidad_a_vender= int(input("Ingrese la cantidad del producto: "))
                valido= False
                if productos[producto][1] > cantidad_a_vender:
                    unidades= productos[producto][1]
                    valido= True
                if not valido:
                    unidades= productos[producto][1]
                    print("El stock del producto es insuficiente, solo hay", unidades, "unidades")
                else:
                    productos[producto][1] -= cantidad_a_vender
                    venta= cantidad_a_vender * productos[producto][2]
                    print("La venta fue de",venta,"pesos")
                    print()
                    venta_diaria.append(venta)
    if opcion == "3":
        """Si elige 3, debe ingresar un valor N, entero positivo (validar sino reingresar), y mostrar los productos que tengan cantidad de 
stock inferior a N."""
        stock_minimo= int(input("Ingrese el stock minimo a controlar: "))
        minimos= []
        if stock_minimo < 0:
            print("El numero ingresado es incorrecto intente nuevamente")
        else:
            for i in productos:
                if productos[i][1] < stock_minimo:
                    producto_minimo= productos[i][1]
                    minimos.append[producto_minimo]
            print("Los productos con stock debajo del minimo son:",minimos)
        print()
    if opcion == "4":
        print()
    if opcion == "5":
        print()
    if opcion == "f" or opcion == "F":
        print()
