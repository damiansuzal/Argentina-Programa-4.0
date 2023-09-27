# Escribir un programa que a partir de una lista de tuplas (Apellido, Nombre, 
# Inicial_segundo_nombre) cree una lista de cadenas
# donde cada una contenga primero el nombre, luego la inicial con un punto, y luego el apellido.
datos = [("Suzal","Damian","A"),("Perez","Willy","S"),("Black","Jack","B")]
lista_cadenas = []
for apellido,nombre,inicial in datos:
    cadena = nombre + " " + inicial + ". " + apellido
    lista_cadenas.append(cadena)
print(lista_cadenas)
