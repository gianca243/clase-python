class Perro:
    patas = 4

    def __init__(self, nombre, edad) -> None:
        self.__nombre = nombre
        self.edad = edad

    def habla(self):
        print(f"{self.__nombre} dice: Guau!")

    @classmethod
    def factory(cls):  # cls hace referencia a la propia clase
        return cls("Chanchito feliz", 4)

    def get_nombre(self):
        return self.__nombre

    def set_nombre(self, nombre):
        self.__nombre = nombre


# Perro.habla() como ya no tiene el decorador para ser un metodo de clase falla

perro1 = Perro.factory()

perro1.habla()

perro1.set_nombre("pipo")

print(perro1.get_nombre())

print(perro1.__dict__)
