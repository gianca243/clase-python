def division(n=0):
    if n == 0:
        raise ZeroDivisionError("no se puede dividir por zero", f"{0}")
    return 5/n


try:
    division()
except ZeroDivisionError as e:
    print(e)
