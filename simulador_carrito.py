def agregar_producto(carrito, producto, precio):
    carrito.append({"producto": producto, "precio": precio})


def mostrar_carrito(carrito):
    total = 0
    for item in carrito:
        print(f"{item['producto']} - ${item['precio']}")
        total += item["precio"]
    print(f"Total: ${total}")


def carrito_compras():
    carrito = []

    while True:
        print("\n1. Agregar producto")
        print("2. Ver carrito")
        print("3. Salir")

        opcion = input("Opción: ")

        if opcion == "1":
            prod = input("Producto: ")
            precio = float(input("Precio: "))
            agregar_producto(carrito, prod, precio)
        elif opcion == "2":
            mostrar_carrito(carrito)
        elif opcion == "3":
            break
        else:
            print("Opción inválida")


carrito_compras()
