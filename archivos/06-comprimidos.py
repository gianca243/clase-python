from pathlib import Path
from zipfile import ZipFile

# with ZipFile("archivos/comprimidos.zip", "w") as zip:
#     for path in Path().rglob("*.*"):
#         print(path)
#         # en caso tal de que el archivo este en windows en vez de usar /
#         #se debe usar \ al momento de revisar o evaluar el nombre del archivo
#         if str(path) != r"archivos\comprimidos.zip":
#             print("omg")
#             zip.write(path)

with ZipFile("archivos/comprimidos.zip") as zip:
    print(zip.namelist())
    info = zip.getinfo("archivos/06-comprimidos.py")
    print(
        info.file_size,
        info.compress_size
    )
    zip.extractall("archivos/descomprimidos")
    