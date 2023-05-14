numeros = (1, 2, 3) + (4, 5, 6)

print(numeros)

punto = tuple([1, 2])
print(punto)
menos_numeros = numeros[:2]
print(menos_numeros)
primero, segundo, *otros = numeros
print(primero, segundo, otros)

for n in numeros:
    print(n)

lista_numeros = list(numeros)
lista_numeros[0] = "chanchito feliz"
print(lista_numeros)
