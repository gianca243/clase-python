from pathlib import Path

archivo = Path("archivos/archivos-prueba.txt")
texto = archivo.read_text("utf-8").split("\n")
texto.insert(0, "hola mundo!")
archivo.write_text("\n".join(texto))
print(texto)
