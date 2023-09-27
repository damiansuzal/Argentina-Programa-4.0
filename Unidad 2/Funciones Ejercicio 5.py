"""Crear una función llamada “Login”, que recibe un nombre de usuario y una contraseña y te devuelve Verdadero 
si el nombre de usuario es “usuario1” y la contraseña es “asdasd”. Además recibe el número de intentos que se ha intentado 
hacer login y si no se ha podido hacer login incremente este valor."""
intentos= 0
def login(usern, passw):
    global intentos
    if usern == "usuario1" and passw == "asdasd":
        print("Acceso concedido despues de {} intentos".format(intentos))
        return True # Login correcto.
        
    else:
        intentos= intentos + 1


usuario= str(input("Ingrese el usuario: "))
contraseña= str(input("Ingrese la contraseña: "))
login(usuario, contraseña)

while not login(usuario, contraseña):
    print("Datos incorrectos, intente nuevamente.")
    usuario= str(input("Ingrese el usuario: "))
    contraseña= str(input("Ingrese la contraseña: "))
    if intentos == 3:
        print("Demasiados intentos incorrectos, su cuenta sera bloqueda de por vida")
        exit(1)