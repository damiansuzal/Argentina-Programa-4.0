""" Modificar el ejercio anterior para poder realizar la suma de dos fracciones de igual denominador. Mostrar el resultado"""
class Fraccion:
    def __init__(self, numerador, denominador):
        self.num = numerador
        self.denom =  denominador

    def mostrar(self):
        print(f"Fracción: {self.num}/{self.denom}")

    def __add__(self, otra_fraccion):
        nuevo_numerador = self.num + otra_fraccion.num
        return Fraccion(nuevo_numerador, self.denom)

numerador= int(input("Ingrese el numerador de 1° fraccion: "))
denominador=int(input ("ingrese el denominador de la 1° fracion: "))
print("Muy bien, ahora ingresemos el numerador de la segunda fraccion")
numerador2= int(input("Ingrese el numerador de 2° fraccion: "))


# Crear un objeto de Fraccion y mostrar sus valores
fraccion1 = Fraccion(numerador, denominador)
fraccion2 = Fraccion(numerador2, denominador)
resultado= fraccion1 + fraccion2
resultado.mostrar()
