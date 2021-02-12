class Pokemon:

    def __init__(self, nome):
        self.__nome = nome

    def cumprimentar(self):
        return f"Eu sou {self.__nome}."


class Aquatico(Pokemon):

    def __init__(self, nome):
        super().__init__(nome)

    def nadar(self):
        return f"{self._Pokemon__nome} está nadando."

    def cumprimentar(self):
        return f"Eu sou {self._Pokemon__nome} do mar."


class Terrestre(Pokemon):

    def __init__(self, nome):
        super().__init__(nome)

    def andar(self):
        return f"{self._Pokemon__nome} está andando."

    def cumprimentar(self):
        return f"Eu sou {self._Pokemon__nome} do terra."


class Hibrido(Aquatico, Terrestre):

    def __init__(self, nome):
        super().__init__(nome)
