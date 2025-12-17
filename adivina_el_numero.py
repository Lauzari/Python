import random


def generar_numero():
    return random.randint(1, 20)


def juego_adivina_numero():
    numero_secreto = generar_numero()
    intentos = 5

    print(" Adivina el número (entre 1 y 20)")

    while intentos > 0:
        intento = input("Ingresa un número: ")

        if not intento.isdigit():
            print("Debes ingresar un número válido.")
            continue

        intento = int(intento)

        if intento == numero_secreto:
            print("¡Correcto! Adivinaste el número.")
            return
        elif intento < numero_secreto:
            print("El número es mayor.")
        else:
            print("El número es menor.")

        intentos -= 1
        print(f"Intentos restantes: {intentos}")

    print(f"Perdiste. El número era {numero_secreto}")


juego_adivina_numero()
