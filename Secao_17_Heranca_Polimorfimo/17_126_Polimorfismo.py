"""
Polimorfismo (objetos que podem possuir muitas formas ou se comportar de formas diferentes)

Quando implementamos novamente um método presente na classe pai em uma subclasse, sobre escrevemos esse
método e isso representa o polimorfismo dos objetos em Python.

"""


class Pokemon:

    def __init__(self, nome):
        self.__nome = nome

    def tipo(self):
        raise NotImplemented("A subclasse precisa implementar essa função.")

    def treinar(self):
        print(f"{self.__nome} está treinando.")


class Aquatico(Pokemon):

    def __init__(self, nome):
        super().__init__(nome)

    def tipo(self):
        print(f"{self._Pokemon__nome} é do tipo aquatico.")


class Terrestre(Pokemon):

    def __init__(self, nome):
        super().__init__(nome)

    def tipo(self):
        print(f"{self._Pokemon__nome} é do tipo terrestre.")


class Fairy(Pokemon):

    def __init__(self, nome):
        super().__init__(nome)

    def tipo(self):
        print(f"{self._Pokemon__nome} é do tipo fada.")


# Testes
ivysaur = Terrestre("ivysaur")
ivysaur.tipo()
ivysaur.treinar()
print("--" * 20)
psyduck = Aquatico("psyduck")
psyduck.tipo()
psyduck.treinar()
print("--" * 20)
rapidash = Fairy("rapidash")
rapidash.tipo()
rapidash.treinar()
print("--" * 20)
