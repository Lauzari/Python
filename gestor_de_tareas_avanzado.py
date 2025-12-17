import json
import os

ARCHIVO = "tareas.json"


def cargar_tareas():
    if not os.path.exists(ARCHIVO):
        return []

    with open(ARCHIVO, "r", encoding="utf-8") as f:
        return json.load(f)


def guardar_tareas(tareas):
    with open(ARCHIVO, "w", encoding="utf-8") as f:
        json.dump(tareas, f, indent=4, ensure_ascii=False)


def agregar_tarea(tareas, descripcion):
    tareas.append({
        "descripcion": descripcion,
        "completada": False
    })
    guardar_tareas(tareas)


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
        guardar_tareas(tareas)
    else:
        print("Índice inválido")


def gestor_tareas():
    tareas = cargar_tareas()

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
