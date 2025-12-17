def validar_contrasena(contrasena):
    if len(contrasena) < 8:
        return False

    tiene_numero = False
    for caracter in contrasena:
        if caracter.isdigit():
            tiene_numero = True

    return tiene_numero


def programa_contrasena():
    contrasena = input("Ingresa una contraseña: ")

    if validar_contrasena(contrasena):
        print("✅ Contraseña válida")
    else:
        print("❌ La contraseña debe tener al menos 8 caracteres y un número")


programa_contrasena()
