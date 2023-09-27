# Definir la tupla “números” con los siguientes números enteros:
# 7, 5, 2, 3, 4, 8, 6, 9, 2
# Buscar y mostrar por pantalla el máximo valor y su posición en la lista utilizando max() e index().
# ¿Qué sucede si quiero hacer lo mismo para obtener el menor valor y su ubicación? Contar y mostrar por pantalla
# la cantidad de veces que aparece el numero 2 con count()
numeros = (7, 5, 2, 3, 4, 8, 6, 9, 2)
maximo = max(numeros)
posicion_max = numeros.index(maximo)
print("El numero maximo es:", maximo,"y esta en la posicion",posicion_max)
minimo = min(numeros)
posicion_min = numeros.index(minimo)
cantidad = numeros.count(minimo)
print("El numero minimo es:", minimo,"y esta en la posicion",posicion_min,"y aparece", cantidad,"veces")
