productos = {}
continua = "s"
while continua == "s":
  codigo= int(input("ingrese el codigo del producto: "))
  descripcion= input("ingrese nombre del producto: ")
  precio= float(input("ingrese precio: "))
  stock= int(input("ingrese stock: "))
  productos[codigo]= [descripcion, precio, stock]
  continua= input("desea cargar mas datos s/n: ")

#muestra del diccionario

for i in productos:
  print("los valores del producto con codigo", i, "nombre:", productos[i][0], "precio:", productos[i][1],"stock:", productos[i][2] )

# busqueda de un codigo de producto
cod=int(input("ingrese el codigo a buscar: "))
if cod in productos:
  print("los valores del producto con codigo: ", "nombre:", productos[i][0], "precio:", productos[i][1],"stock:", productos[i][2])
else:
  print(" no se encontro ese codigo ")

#listar los productos con stock cero

for i in productos:
  if productos[i][2]==0:
    print("los valores del producto con stock cero son", i, productos[i][0], productos[i][1],productos[i][2] )