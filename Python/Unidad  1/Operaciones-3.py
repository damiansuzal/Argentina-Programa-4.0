# Pedir peso y altura para calcular la masa corporal: mc = peso / altura^2.
peso = float(input("Ingrese su peso en kg: "))
altura = float(input("Ingrese su altura en mts: "))

# Calulo
imc = peso / (altura ** 2)

print("Su indice de masa corporal es: ", imc)
