""" Crear una clase de nombre Gelatina La clase Gelatina recibirá como argumentos el tamaño en gramos, el color y el sabor
Definir un método para mostrar las propiedades, Crear tres objetos y mostrar las propiedades"""
class Gelatina:
    def __init__(self, tamaño, color):
        self.tamaño= tamaño
        self.color= color

    def mostrar(self):
        print(f"El tamaño es de {self.tamaño} y es de color {self.color}")

tamaño= input("Ingrese el tamaño de la 1° gelatina en gramos: ")
color = input ("Ingrese el color de la gelatina :")
ge1=Gelatina (int(tamaño), str(color)) # aca se crea el objeto o se instancia la clase
print("\nPropiedades del primer objeto:")
ge1.mostrar() # se usa el objeto
print()
#----------------------------------------
tamaño2= input("Ingrese el tamaño de la 2° gelatina en gramos: ")
color2 = input ("Ingrese el color de la gelatina :")
ge2=Gelatina (int(tamaño2), str(color2)) # aca se crea el objeto o se instancia la clase
print("\nPropiedades del segundo objeto:")
ge2.mostrar() # se usa el objeto
print()
#----------------------------------------
tamaño3= input("Ingrese el tamaño de la 3° gelatina en gramos: ")
color3 = input ("Ingrese el color de la gelatina :")
ge3=Gelatina (int(tamaño3), str(color3)) # aca se crea el objeto o se instancia la clase
print("\nPropiedades del tercer objeto:")
ge3.mostrar() # se usa el objeto
print()
#----------------------------------------

        

    