""" Crear una clase de nombre fraccion que reciba como argumentos dos valores correspondientes al numerador y al denorminador 
de una fracción, Crear un objeto de fracción y mostrar el numerador y el denominador"""
class Fraccion:
    def __init__(self, numerador, denominador):
        self.num = numerador
        self.denom =  denominador

    def mostrar(self):
        print(f"Fracción: {self.num}/{self.denom}")

numerador= input("Ingrese el numerador de la fraccion: ")
denominador=input ("ingrese el denominador de la fracion: ")

# Crear un objeto de Fraccion y mostrar sus valores
fraccion1 = Fraccion(numerador, denominador)
fraccion1.mostrar()




