class Caminador:
    def caminar(self):
        print("caminando")


class Volador:

    def volar(self):
        print("volando")


class Nadador:

    def nadar(self):
        print("nadando")


class Pato(Caminador, Nadador, Volador):

    def programar(self):
        print("programando")


chanchito = Pato()
chanchito.volar()
