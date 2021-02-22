"""
28) Baseando-se no exercício 27 adicione os métodos ligar e desligar que deverão mudar o conteúdo
do atributo ligado conforme o caso.
"""

from ex_27 import Microondas1


class Microondas2(Microondas1):

    def __init__(self):
        super().__init__()

    def ligar(self):
        if self.ligado:
            print("\nO micro ondas já está ligado.")
        else:
            self.set_ligado = True

    def desligar(self):
        if self.ligado:
            self.set_ligado = False
        else:
            print("\nO micro ondas já está desligado.")


if __name__ == "__main__":

    m1 = Microondas2()
    m1.imprimir()
    print("_" * 90, end="\n")
    m1.ligar()
    m1.imprimir()
    print("_" * 90, end="\n")
    m1.desligar()
    m1.imprimir()

