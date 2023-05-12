numeros = [2, 4, 1, 45, 75, 22]

numeros.sort(reverse=True)
omg = sorted(numeros)
print(omg)
print(numeros)

usuarios = [
    [5, "chanchito"],
    [2, "monguito"],
    [3, "pulga"]
]


def ordena(elemento):
    return elemento[0]


# usuarios.sort(key=ordena)
usuarios.sort(key=lambda item: item[0], reverse=True)
print(usuarios)
