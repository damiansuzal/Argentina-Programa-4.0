# Definir como constantes MAX y MIN con valores de 50 y 25 respectivamente. Luego, ingresar una temperatura temp por teclado y decir:
# hace calor ( cuando es igual o superior a 50 temp>=50)
# está templado cuando es mayor o igual a 25 y menor que 50.
# hace frio si es menor a 25.
MAX= 40
MIN= 20
temp = float(input("Ingrese una temperatura: "))
if temp >= MAX:
    print("Hace Calor!")
elif temp >= MIN and temp < MAX:
    print("Esta templado!")
else:
    print("Hace frio!")



