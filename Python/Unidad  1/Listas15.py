# Escribir un programa que almacene los vectores (1,2,3) y (-1,0,2) en dos listas y muestre por 
# pantalla su producto escalar.
vector1= [1,2,3]
vector2= [-1,0,2]
producto_escalar= 0
for i in range (len(vector1)):
    producto_escalar += vector1[i] * vector2[i]
print("El producto escalar es:", producto_escalar)
