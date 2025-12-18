import random


def obtener_palabra_secreta() -> str:
    palabras = ["gato", "perro", "rana", "ave","rata", "tigre", "elefante", "jirafa", "mono", "leon"]
    return random.choice(palabras)


def mostrar_progreso(palabra_secreta, letras_adivinadas):
    adivinado = ""
    for letra in palabra_secreta:
        if letra in letras_adivinadas:
            adivinado += letra
        else:
            adivinado += "_"
    return adivinado


def juego_ahorcado():
    palabra_secreta = obtener_palabra_secreta()
    letras_adivinadas = []
    intentos = 15
    juego_terminado = False

    print("¡Bienvenido al juego del ahorcado!")
    print(f"Tenés {intentos} intentos para adivinar la palabra secreta")

    while not juego_terminado and intentos > 0:
        print(mostrar_progreso(palabra_secreta, letras_adivinadas))
        adivinanza = input("Ingresa una letra: ").lower()

        if len(adivinanza) != 1 or not adivinanza.isalpha():
            print("Por favor introduzca una letra válida.")
        elif adivinanza in letras_adivinadas:
            print("Ya has adivinado esa letra.")
        else:
            letras_adivinadas.append(adivinanza)

            if adivinanza in palabra_secreta:
                print(f"¡Bien! La letra {adivinanza} está en la palabra.")
            else:
                intentos -= 1
                print(f"Lo siento, la letra {adivinanza} no está.")
                print(f"Te quedan {intentos} intentos.")

        progreso_actual = mostrar_progreso(palabra_secreta, letras_adivinadas)
        if "_" not in progreso_actual:
            juego_terminado = True
            print(f"¡Felicidades! Adivinaste la palabra: {palabra_secreta}")

    if intentos == 0:
        print(f"Perdiste 😢 La palabra era: {palabra_secreta}")


juego_ahorcado()
