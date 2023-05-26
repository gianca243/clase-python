class MyError(Exception):
    "Esta clase es para representar mi error"

    def __init__(self, mensaje, codigo) -> None:
        self.mensaje = mensaje
        self.codigo = codigo

    def __str__(self) -> str:
        return f"{self.mensaje} - codigo: {self.codigo}"


def division(n=0):
    if n == 0:
        raise MyError("no se puede dividir por zero", 805)
    return 5/n


try:
    division()
except MyError as e:
    print(e)
