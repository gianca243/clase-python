class Perro:
    def __init__(self, nombre) -> None:
        self.nombre = nombre

    @property
    def nombre(self):
        print("pasando por el getter")
        return self.__nombre

    @nombre.setter
    def nombre(self, nombre):
        print("pasando por el setter")
        if nombre.strip():
            self.__nombre = nombre
        return


perro = Perro("choclo")
print(perro.nombre)
