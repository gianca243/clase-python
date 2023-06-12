import csv
import os
# with open("archivos/archivo.csv", "w") as archivo:
#     writer = csv.writer(archivo, dialect='unix')
#     writer.writerow(["twit_id", "user_id", "text"])
#     writer.writerow([1000, 1, "este es un twit"])
#     writer.writerow([1001, 2, "omg"])

# with open("archivos/archivo.csv") as archivo:
#     reader = csv.reader(archivo)
#     print(list(reader))
#     archivo.seek(0)
#     for linea in reader:
#         print(linea)

# actualizar

with open("archivos/archivo.csv") as r, open("archivos/archivo_temp.csv", "w") as w:
    reader = csv.reader(r)
    writer = csv.writer(w, dialect='unix')
    for linea in reader:
        if linea[0] == "1000":
            writer.writerow([1000, 1, "este es un texto nuevo"])
        else:
            writer.writerow(linea)
# en windows como no puedes eliminar un archivo mientras esta abierto
# asi que para poder remover el archivo tenemos que cerrar el archivo
# o eliminarlo despues del open que se encarga de cerrar el documento
os.remove("archivos/archivo.csv")
os.rename("archivos/archivo_temp.csv", "archivos/archivo.csv")
