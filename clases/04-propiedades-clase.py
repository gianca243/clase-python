class Perro:
    patas = 4  # propiedades de la clase

    def __init__(self, nombre, edad) -> None:
        self.nombre = nombre  # propiedades de la instancia de la clase
        self.edad = edad
        # print(nombre)

    # metodos

    def habla(self) -> None:
        print(f"{self.nombre} dice: Guau!")


Perro.patas = 3
mi_perro = Perro("pipo", 4)
mi_perro.patas = 5
mi_perro2 = Perro("annie", 4)
print(Perro.patas)
print(mi_perro.patas)
print(mi_perro2.patas)
# mi_perro.habla()
# print(mi_perro.nombre)
