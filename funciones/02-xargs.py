from functools import reduce


def suma(*numeros):
    result = reduce(lambda a, b: a + b, numeros)
    print(result)


def suma_v2(*args):
    result = 0
    for num in args:
        result += num
    print(result)


suma(2, 5)
suma(2, 5, 6)
suma_v2(2, 5, 34, 543, 54, 44, 1)
