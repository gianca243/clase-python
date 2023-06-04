if __name__ != "__main__":
    from ..gestion.crud import guardar
# from ..gestion.crud import guardar
# todo: investigar el uso de rutas relativas
# rsult: fallaba porque se estaba ejecutando este archivo
print(__name__)


def pagar_impuestos():
    print("pagando impuestos")
