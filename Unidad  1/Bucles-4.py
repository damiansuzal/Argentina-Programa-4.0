# Calcula e imprime el producto de la serie 2x4x6x8x … x20.
product=1
for i in range(2,20,2):
    product=product*i
    print("El producto es: ", product)
