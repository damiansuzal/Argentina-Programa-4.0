# Escribir un programa que permita cargar las temperaturas del mes. Luego debe recorrer la lista y calcular:
# a) La temperatura promedio del mes. b) La temperatura máxima y el día en que ocurrió c) La temperatura mínima,
# y el día en que ocurrió d) la cantidad de días con temperaturas mayores al promedio.
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


temperatura_promedio= float(promedio / len(temperaturas_mes))
for temperatura in temperaturas_mes:
    if temperatura > temperatura_promedio:
        cantidad_dias_calurosos += 1
print("La temperatura promedio del mes es de", temperatura_promedio,"º")
print("La temperatura maxima ocurrio el dia", dia_maximo,"y fue de", temperatura_maxima,"º" )
print("La temperatura minima fue de", temperatura_minima,"º" )
print("La cantidad de dias calurosos fue de", cantidad_dias_calurosos )

