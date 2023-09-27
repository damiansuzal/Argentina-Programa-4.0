"""Ejercicio: Contar la frecuencia de palabras en una lista
Escribe un programa que tome una lista de palabras como entrada y cuente la frecuencia 
de cada palabra en la lista. Luego, muestra el resultado, es decir, las palabras junto con 
su frecuencia."""
palabras = ['manzana', 'banana', 'manzana', 'naranja', 'manzana', 'uva', 'uva', 'manzana']
frecuencia = {}

for palabra in palabras:
    if palabra in frecuencia:
        frecuencia[palabra] += 1
    else:
        frecuencia[palabra] = 1

for palabra, count in frecuencia.items():
    print(f'{palabra}: {count}')
