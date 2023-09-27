"""DICCIONARIOS CON LISTAS - Crear un programa que permita guardar el stock de un conjunto de productos de un negocio.
Los datos a almacenar son el nombre del producto (clave) y para cada producto tenemos los siguientes valores: peso unitario del producto (valor real), cantidad (valor entero), precio del producto (valor real).
Se debe presentar un menú
1) Cargar un producto
2) Vender un producto
3) Listar cantidad de productos con stock mínimo debajo de N
4) Calcular el monto total vendido en el día
5) Baja de un producto
f o F) Fin del programa
Si elige 1, se deberá cargar un producto al diccionario. Se carga la clave y la lista con los valores de peso, cantidad y precio. Si los valores ingresados son negativos o cero se debe solicitar reingreso SOLO del valor incorrecto. Ver que si la clave ya existe en el diccionario puede modificar los valores.
Si elige 2, debe ingresar un nombre de producto y la cantidad a vender de ese producto, luego debe descontar la cantidad vendida del stock y mostrar el total de la venta. Si no se puede vender, por que NO hay stock suficiente o porque el producto no existe se debe mostrar un cartel. Las ventas del día (total) se deben ir guardando en una lista que se utilizará en el punto 4.
Si elige 3, debe ingresar un valor N, entero positivo (validar sino reingresar), y mostrar los productos que tengan cantidad de stock inferior a N.
Si elige 4, utiliza la lista que contiene los totales de cada venta y muestra la cantidad de ventas realizadas y total de todas las ventas.
Si elige 5, debe ingresar un nombre de producto y, si existe la clave elimina el producto y muestra un cartel: "Se eliminó el producto". Si no existe la clave se muestra un cartel "No existe el producto a eliminar"."""