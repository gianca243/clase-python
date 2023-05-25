class Animal:
    def comer(self):
        print("comiendo")


class Perro(Animal):

    def pasear(self):
        print("pasear")


perro = Perro()
perro.comer()


class Chanchito(Perro):

    def programar(self):
        print("programando")


chanchito = Chanchito()
chanchito.pasear()
