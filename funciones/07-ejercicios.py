def reverse(text: str):
    word = ""
    for index in range(len(text)):
        word += text[(index + 1) * -1]
    return word


def cool_reverse(text: str):
    word = ""
    for char in text:
        word = char + word
    return word


def es_palindromo(texto: str):
    texto = texto.replace(" ", "").lower()
    word = cool_reverse(texto)
    message = "no es palindromo"
    if word == texto:
        message = "si es palindromo"
    return message


print(es_palindromo("la tele letal"))
