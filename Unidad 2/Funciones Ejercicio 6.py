""" Crear un programa principal donde se pida un nombre de usuario y una contraseña y se intente hacer login, 
solamente tenemos tres oportunidades para intentarlo."""
intentos= 0
def login(usern, passw):
    global intentos
    if usern == "admin" and passw == "1234":
        print("Acceso concedido")
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