"""
POO - O método super()

O método super() se refere á super classe.

class Animal:

    def __init__(self, nome, especie):
        self.__nome = nome
        self.__especie = especie

    def emite_som(self, som):
        print(f"O {self.__nome} emite um {som}.")


class Gato(Animal):

    def __init__(self, nome, especie, raca):
        super().__init__(nome, especie)
        self.__raca = raca


geromel = Gato("Geromel", "Felino", "Maine Coon")
geromel.emite_som("miado")

"""


