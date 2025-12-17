import random
import string


def generar_contrasena(longitud):
    caracteres = string.ascii_letters + string.digits
    contrasena = ""

    for _ in range(longitud):
        contrasena += random.choice(caracteres)

    return contrasena


def programa_generador():
    longitud = int(input("Longitud de la contraseña: "))
    print(" Contraseña generada:")
    print(generar_contrasena(longitud))


programa_generador()
