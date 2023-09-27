""" Crear una función que calcule la temperatura media de un día a partir de la temperatura máxima y mínima. 
Crear un programa principal, que utilizando la función anterior, vaya pidiendo la temperatura máxima y mínima de cada día y vaya 
mostrando la media. El programa pedirá el número de días que se van a introducir."""
def temperatura_promedio(minimo, maximo):
    return (minimo + maximo) / 2

n = int(input("Introduce el numero de dias: ")) # pedimos al usuario cuantos datos va a ingresar
for i in range (n):
    tmax= float(input("Ingrese la temperatura máxima del día {}: ".format(i + 1))) # ingresamos cada dato como float en la variable "tmax"
    tmin= float(input("Ingrese la temperatura minima del día {}: ".format(i + 1))) # ingresamos cada dato como float en la variable "tmin"
    prom= temperatura_promedio(tmax, tmin)
    print("La temperatura media del dia {} es {}.".format(i + 1, prom))


        

