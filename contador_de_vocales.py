def contar_vocales(texto):
    vocales = "aeiou"
    contador = 0

    for letra in texto.lower():
        if letra in vocales:
            contador += 1

    return contador


def programa_contador_vocales():
    texto = input("Ingresa una frase: ")
    resultado = contar_vocales(texto)
    print(f"La frase tiene {resultado} vocales.")


programa_contador_vocales()
