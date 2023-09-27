"""Definir una función inversa() que calcule la inversión de una cadena. 
Por ejemplo la cadena "estoy probando" debería devolver la cadena "odnaborp yotse"""
def invertido(cad):
    return cad[::-1]

# devuelve el string con los caracteres en orden contrario a como están escritos
cadena= input(str("Ingrese una cadena para invertir: "))
invertida= invertido(cadena)
print('La cadena invertida es: ','"', invertida, '"')