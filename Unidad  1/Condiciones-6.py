lado1 = int(input("Ingrese un lado del triangulo: "))
lado2 = int(input("Ingrese otro lado del triangulo: "))
lado3 = int(input("Ingrese el ultimo lado del triangulo: "))
if lado1 + lado2 > lado3 and lado2 + lado3 > lado1 and lado3 + lado1 > lado2: #valido que sea un triangulo
    if lado1 == lado2 == lado3:
        print("Es un triangulo Equilatero")

    if lado1 != lado2 and lado1 != lado3 and lado2 != lado3:
        print("Es un triangulo Escaleno")

    if lado1 == lado2 != lado3 or lado1 != lado2 == lado3 or lado1 == lado3 != lado2:
        print("Es un triangulo Isoceles")
else:
    print("No es un triangulo valido")
