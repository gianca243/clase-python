import os
import sys
from pathlib import Path

# print(sys.argv)

#  python .\modulos-nativos\05-cli.py -a holamundo
#   ['.\\modulos-nativos\\05-cli.py', '-a', 'holamundo']


def cli(args):
    if len(args) == 1:
        print("no se paasron argumentos")
        return
    if len(args) != 3:
        print("se necesitan dos argumentos")
        return

    origen = args[1]
    o = Path(origen)
    if not o.exists():
        print("Origen no existe")
        return

    destino = args[2]
    d = Path(destino)
    if d.exists():
        print("destino no puede existe")
        return

    os.rename(str(origen), str(destino))
    print("archivo renombrado con exito")


cli(sys.argv)
