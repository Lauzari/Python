def mostrar_lista(lista):
    if not lista:
        print("La lista está vacía.")
    else:
        for i, item in enumerate(lista, 1):
            print(f"{i}. {item}")


def lista_compras():
    compras = []

    while True:
        print("\n1. Agregar producto")
        print("2. Mostrar lista")
        print("3. Salir")

        opcion = input("Elige una opción: ")

        if opcion == "1":
            producto = input("Nombre del producto: ")
            compras.append(producto)
        elif opcion == "2":
            mostrar_lista(compras)
        elif opcion == "3":
            print("👋 Saliendo...")
            break
        else:
            print("Opción inválida.")


lista_compras()
