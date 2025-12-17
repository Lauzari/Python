def agregar_contacto(contactos, nombre, telefono):
    contactos[nombre] = telefono


def mostrar_contactos(contactos):
    if not contactos:
        print("No hay contactos guardados.")
        return

    for nombre, telefono in contactos.items():
        print(f"{nombre}: {telefono}")


def gestor_contactos():
    contactos = {}

    while True:
        print("\n1. Agregar contacto")
        print("2. Mostrar contactos")
        print("3. Salir")

        opcion = input("Opción: ")

        if opcion == "1":
            nombre = input("Nombre: ")
            telefono = input("Teléfono: ")
            agregar_contacto(contactos, nombre, telefono)
        elif opcion == "2":
            mostrar_contactos(contactos)
        elif opcion == "3":
            print(" Hasta luego")
            break
        else:
            print("Opción inválida")


gestor_contactos()
