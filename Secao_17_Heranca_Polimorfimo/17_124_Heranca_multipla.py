"""
Herança Múltipla

Uma classe pode herdar todos os atributos e métodos de mais de uma classe. Não importa se a herança ocorre
por qualquer um dos dois métodos possíveis, a classe herdeira acessa todos os métodos das demais. Formas que
podem ser feitas as heranças:

- Multi derivação direta

class Base1:
    pass


class Base2:
    pass


class Base3:
    pass


class SubClass(Base1, Base2, Base3):
    pass


- Multi derivação indireta:

class Base1:
    pass


class Base2(Base1):
    pass


class Base3(Base2):
    pass


class SubClass(Base3):
    pass


"""


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


squirtle = Aquatico("Squirtle")
print(squirtle.nadar())
print(squirtle.cumprimentar())
print("-" * 20)
golem = Terrestre("Golem")
print(golem.andar())
print(golem.cumprimentar())
print("-" * 20)
quagsire = Hibrido("Guagsire")
print(quagsire.andar())
print(quagsire.nadar())
# é executado o cumprimento aquatico, pois é a primeira classe a ser herdada
# esse comportamento está relacionado com o MRO - Method Order Resolution
# ou seja, a ordem de herança afeta o comportamento do objeto herdeiro
print(quagsire.cumprimentar())
print("-" * 20)

# Descobrindo as origens dos objetos:
print(f"Guagsire é instância de Hibrido? {isinstance(quagsire, Hibrido)}")
print(f"Guagsire é instância de Terrestre? {isinstance(quagsire, Terrestre)}")
print(f"Guagsire é instância de Aquatico? {isinstance(quagsire, Aquatico)}")
print(f"Guagsire é instância de Pokemon? {isinstance(quagsire, Pokemon)}")
# em Python por padrão qualquer classe herda de object por padrão
print(f"Guagsire é instância de object? {isinstance(quagsire, object)}")
