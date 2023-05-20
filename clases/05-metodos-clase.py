class Perro:
    patas = 4

    def __init__(self, nombre, edad) -> None:
        self.nombre = nombre
        self.edad = edad

    @classmethod
    def habla(cls):  # cls hace referencia a la propia clase
        print("Guau!")

    @classmethod
    def factory(cls):
        return cls("Chanchito feliz", 4)


Perro.habla()

mi_perro = Perro.factory()
mi_perro.habla()
