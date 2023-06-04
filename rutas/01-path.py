from pathlib import Path

# Path(r"C:\Archivos de programa\Minecraft")
# Path("/usr/bin")  # absoluta
# Path()
# Path.home()
# Path("one/__init__.py")  # ruta relativa


path = Path("hola-mundo/mi-archivo.py")
path.is_file()  # pregunta si es archivo
path.is_dir()  # pregunta si es carpeta
path.exists()  # pregunta si el archivo o directorio existe

print(
    path.name,
    path.stem,
    path.suffix,
    path.parent,
    path.absolute()
)

p = path.with_name("chanchito.exe")
print(p)
p = path.with_suffix(".bat")
print(p)
p = path.with_stem("feliz")
print(p)
