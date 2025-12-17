def validar_nombre(nombre):
    return len(nombre) >= 3


def validar_email(email):
    return "@" in email and "." in email


def validar_edad(edad):
    return edad.isdigit() and int(edad) >= 18


def formulario():
    nombre = input("Nombre: ")
    email = input("Email: ")
    edad = input("Edad: ")

    if not validar_nombre(nombre):
        print("Nombre inválido")
    elif not validar_email(email):
        print("Email inválido")
    elif not validar_edad(edad):
        print("Debes ser mayor de 18")
    else:
        print("✅ Formulario válido")


formulario()
