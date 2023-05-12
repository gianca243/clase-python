# numeros = [1, 2, 3]

# feo
# primero = numeros[0]
# segundo = numeros[1]
# tercero = numeros[2]

# primero, segundo, tercero = numeros
# print(primero, segundo, tercero)

# primero, *otros = numeros
# print(primero, otros)

numeros = list(range(1, 10))
primero, *otros, ultimo = numeros
print(primero, *otros, ultimo)
