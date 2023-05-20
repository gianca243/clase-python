class Perro:
    def __init__(self, nombre, edad) -> None:
        self.nombre = nombre
        self.edad = edad
        # print(nombre)

    # metodos

    def habla(self) -> None:
        print(f"{self.nombre} dice: Guau!")


mi_perro = Perro("pipo", 4)
mi_perro.habla()
# print(mi_perro.nombre)
