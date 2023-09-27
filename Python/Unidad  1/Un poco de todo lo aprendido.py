# CUENTA CANTIDAD DE PALABRAS DE UNA LISTA A UN DICCIONARIO
palabras = ['manzana', 'banana', 'manzana', 'naranja', 'manzana', 'uva', 'uva', 'manzana']
frecuencia = {}

for palabra in palabras:
    if palabra in frecuencia:
        frecuencia[palabra] += 1
    else:
        frecuencia[palabra] = 1

for palabra, count in frecuencia.items():
    print(f'{palabra}: {count}')
#-----------------------------------------------------------
# CREA UN DICCIONARIO CON N VALORES, CON NOMBRE Y TELEFONO
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
#-----------------------------------------------------------
# FUNCION PARA CARGAR UN PRODUCTO
def cargar_producto(stock): #funcion que carga el producto
    clave = input("Ingrese el nombre del producto: ")
    peso = -1 
    while peso <= 0:
        peso = float(input("Ingrese el peso unitario del producto: "))
        if peso <= 0:
            print("El peso debe ser un valor numérico positivo.")
            print()

#-----------------------------------------------------------
# FUNCION PARA DESCONTAR UN PRODUCTO
def vender_producto(stock, ventas): 
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

#-----------------------------------------------------------
# PROGRAMA QUE CARGA LAS TEMPERATURAS DEL MES
temperaturas_mes= []
temperatura_promedio= 0
temperatura_maxima= 0
temperatura_minima= 100
dia_maximo= 0
cantidad_dias_calurosos= 0
promedio= 0
for i in range (5):
    grados= int(input("Ingrese la temperatura del dia " + str(i+1) + ": "))
    temperaturas_mes.append(grados)
    promedio += grados
    if grados > temperatura_maxima:
        temperatura_maxima= grados
        dia_maximo = i+1
    if grados < temperatura_minima:
        temperatura_minima= grados

#-----------------------------------------------------------
# CONTADOR DE LISTAS
lista=[1,4,4,5,9,4,6,4,8,7,3,4]
contador=0
num=int(input("Ingrese un numero: "))
for numero in lista:
    if num == numero:
        contador= contador + 1
print("El numero",num, "se repite", contador,"veces.")

#-----------------------------------------------------------
# TUPLA QUE CREA UNA LISTA DE TUPLAS A PARTIR DE UNA LISTA
datos = [("Suzal","Damian","A"),("Perez","Willy","S"),("Black","Jack","B")]
lista_cadenas = []
for apellido,nombre,inicial in datos:
    cadena = nombre + " " + inicial + ". " + apellido
    lista_cadenas.append(cadena)
print(lista_cadenas)

#-----------------------------------------------------------
# DEFINIR TUPLA Y BUSCAR NUMIMOS Y CONTAR
numeros = (7, 5, 2, 3, 4, 8, 6, 9, 2)
maximo = max(numeros)
posicion_max = numeros.index(maximo)
print("El numero maximo es:", maximo,"y esta en la posicion",posicion_max)
minimo = min(numeros)
posicion_min = numeros.index(minimo)
cantidad = numeros.count(minimo)
print("El numero minimo es:", minimo,"y esta en la posicion",posicion_min,"y aparece", cantidad,"veces")

#-----------------------------------------------------------
# CARGAR UN DICCIONARIO Y RECORRERLO
dicc={}
n= int(input("Ingrese la cantidad de elementos a cargar: ")) # pide la cantidad de elementos a agregar
for i in range(n): # pide la cantidad de n veces, la clave y el valor del elemento actual
    clave= input("Ingrese la clave del elemento nº" + str(i+1) + ": ")
    valor= input("Ingrese el valor del elemento nº" + str(i+1) + ": ")
    dicc[clave]= valor # agrega el elemento al diccionario
print(dicc)
print() # linea vacia
print("El diccionario tiene", len(dicc), "elementos")
print() # linea vacia
for clave in dicc: # muestra solo las claves
    print(clave)
print() # linea vacia
dicc["clavenueva"]= n + 1
dicc_copia= dicc.copy() # copia un diccionario a otro
print("Diccionario dicc:" ,dicc)
print("Diccionario dicc_copia:" ,dicc_copia)
del dicc # elimina el diccionario
print("El Diccionario dicc ah sido eliminado:")


