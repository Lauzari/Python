def agregar_tarea(tareas, descripcion):
    tareas.append({"descripcion": descripcion, "completada": False})


def mostrar_tareas(tareas):
    if not tareas:
        print("No hay tareas.")
        return

    for i, tarea in enumerate(tareas, 1):
        estado = "✔" if tarea["completada"] else "❌"
        print(f"{i}. {tarea['descripcion']} [{estado}]")


def completar_tarea(tareas, indice):
    if 0 <= indice < len(tareas):
        tareas[indice]["completada"] = True
    else:
        print("Índice inválido")


def gestor_tareas():
    tareas = []

    while True:
        print("\n1. Agregar tarea")
        print("2. Mostrar tareas")
        print("3. Completar tarea")
        print("4. Salir")

        opcion = input("Opción: ")

        if opcion == "1":
            desc = input("Descripción: ")
            agregar_tarea(tareas, desc)
        elif opcion == "2":
            mostrar_tareas(tareas)
        elif opcion == "3":
            mostrar_tareas(tareas)
            num = int(input("Número de tarea: ")) - 1
            completar_tarea(tareas, num)
        elif opcion == "4":
            break
        else:
            print("Opción inválida")


gestor_tareas()
