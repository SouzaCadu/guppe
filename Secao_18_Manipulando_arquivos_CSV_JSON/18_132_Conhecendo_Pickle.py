"""
Arquivos Pickle

Salva os dados em formato binário, hexadecimal. Realiza o processo de binarização de qualquer objeto Python,
também chamado de serialização e deserialização. Não é seguro contra códigos maliciosos, deve ser evitado para
lidar com arquivos de terceiros.

"""

import pickle


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

golem = Terrestre("Golem")

quagsire = Hibrido("Guagsire")

with open("pokemon.pickle", "wb") as arquivo:
    pickle.dump((squirtle, golem, quagsire), arquivo)

with open("pokemon.pickle", "rb") as arquivo:
    squirtle, golem, quagsire = pickle.load(arquivo)
    # lendo os objetos a partir do arquivo pickle.
    print(squirtle.nadar())
    print(squirtle.cumprimentar())
    print("-" * 20)
    print(golem.andar())
    print(golem.cumprimentar())
    print("-" * 20)
    print(quagsire.andar())
    print(quagsire.nadar())
    print("-" * 20)

