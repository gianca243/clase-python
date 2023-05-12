usuarios = [
    ["chanchito", 1],
    ["monguito", 6],
    ["pulga", 5]
]
nombres = [usuario[0] for usuario in usuarios]

nombres = [usuario[0] for usuario in usuarios if usuario[1] > 2]
print(nombres)
