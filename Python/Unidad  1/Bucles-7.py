#Escribir un programa que permita
#ingresar un número N (entero positivo, si se ingresa otra cosa, mostrar un error)
#ingresar un número X (real positivo que debe estar entre 0 y π , si se ingresa otra cosa,mostrar un error)
#luego calcular y mostrar la aproximación al Seno del ángulo X
#como Sen (X) = (𝑥 - 𝑥3 / 3 ! + x5 / 5 ! - x7 / 7 ! + …)
#NOTA: N expresa la cantidad de términos a considerar en la serie de Taylor,
#utilizada para aproximar el Seno de X. Verificar que... a mayor N se obtiene una mejor aproximación.
numn=-1
numx=-1
while numn<0:  #mientras se ingrese el numero incorrecto se sigue pidiendo el numero otra vez
    numn= int(input("Ingrese un numero entero: "))
    if numn<0:
        print("El numero ingresado es negativo, ingrese un numero positivo")

while numx<0 or numx>3.141592:  #mientras se ingrese el numero incorrecto se sigue pidiendo el numero otra vez
    numx= float(input("Ingrese un numero real: "))
    if numx<0 or numx>3.141592:
        print("El numero ingresado esta fuera del rango correcto, ingrese un numero entre 0 y Pi")

# Calcular la aproximación del seno
seno_aproximado = 0
for i in range(N):
    termino = ((-1) ** i) * (X ** (2 * i + 1)) / math.factorial(2 * i + 1)
    seno_aproximado += termino

# Mostrar el resultado
print("La aproximación del seno de", X, "es:", seno_aproximado)

