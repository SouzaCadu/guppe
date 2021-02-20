"""
22) Baseando-se no exercicio 21 adicione os métodos ligar e desligar que deverão mudar o conteúdo do atributo ligado
conforme o caso
"""

from ex_21 import Televisor1


class Televisor2(Televisor1):

    def __init__(self):
        super().__init__()
        self.__set_ligado = False

    def ligar(self):
        if self.__set_ligado:
            print("O televisor já está ligado.")
        else:
            self.__set_ligado = True

    def desligar(self):
        if not self.__set_ligado:
            print("O televisor já está desligado.")
        else:
            self.__set_ligado = False

    def imprimir(self):
        if self.__set_ligado:
            print(f"\nO televisor está ligado no canal {self.canal} no volume {self.volume}.")
        else:
            print("\nO televisor encontra-se desligado.")


if __name__ == "__main__":

    tv3 = Televisor2()
    tv3.set_volume = 20
    tv3.set_canal = 6
    tv3.ligar()
    tv3.imprimir()
    print("_" * 90, end="\n")
    tv3.desligar()
    tv3.imprimir()
