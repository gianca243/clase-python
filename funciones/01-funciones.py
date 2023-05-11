# nombre es un parametro
def hola(nombre, apellido=""):
    print("hola mundo")
    print(f"bienvenido {nombre} {apellido}")


# los valores que recibe la funcion son argumentos
hola("gian", "zapata")

hola(nombre="gian", apellido="zapata")
