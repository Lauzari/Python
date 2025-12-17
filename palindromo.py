def es_palindromo(texto):
    texto = texto.lower().replace(" ", "")
    return texto == texto[::-1]


def programa_palindromo():
    palabra = input("Ingresa una palabra o frase: ")

    if es_palindromo(palabra):
        print("✅ Es un palíndromo")
    else:
        print("❌ No es un palíndromo")


programa_palindromo()
