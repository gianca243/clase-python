# class Perro:
#     def __init__(self, Correa) -> None:
#         self.correa = Correa()
# import usuario

# def guardar():
#     usuario.guardar() # sin it¿yeccion de dependencias

# def guardar(entidad):
#     entidad.guardar()

# def init_app(bbdd, api):
#   inicializacion de modulo

from pathlib import Path

path = Path()
paths = [p for p in path.iterdir() if p.is_dir()]

dependencias = {
    "db": "base de datos",
    "api": "esta es la api",
    "graphql": "esto es graphql"
}


def load(p):
    print(str(p))
    paquete = __import__(str(p).replace("/", "."))
    try:
        paquete.init(**dependencias)
    except:
        print("el paquete no se encontro")


list(map(load, paths))
