def sacar_turno(turnos, nombre):
    turnos.append(nombre)
    print(f"Turno asignado a {nombre}")


def atender_turno(turnos):
    if turnos:
        persona = turnos.pop(0)
        print(f"Atendiendo a {persona}")
    else:
        print("No hay turnos pendientes")


def sistema_turnos():
    turnos = []

    while True:
        print("\n1. Sacar turno")
        print("2. Atender turno")
        print("3. Salir")

        opcion = input("Opción: ")

        if opcion == "1":
            nombre = input("Nombre: ")
            sacar_turno(turnos, nombre)
        elif opcion == "2":
            atender_turno(turnos)
        elif opcion == "3":
            break
        else:
            print("Opción inválida")


sistema_turnos()
