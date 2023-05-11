saludo = "hola global"
omg = 1


def saludar():
    print(omg)
    saludo = "Hola mundo"
    print(saludo)
    return saludo


def saluda_chanchito():
    # global saludo no hacer
    saludo = "Hola chancito"
    print(saludo)
    return saludo


saludar()
saluda_chanchito()
saludar()
