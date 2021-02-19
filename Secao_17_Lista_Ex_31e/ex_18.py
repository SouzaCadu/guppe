"""
18) Baseando-se no exercício 17 adicione um método construtor que permita
a definição de todos os atributos no momento da instanciação do objeto.
"""

from ex_17 import Eletrodomestico


class Eletrodomestico1(Eletrodomestico):

    def __init__(self):
        super().__init__(ligado=False)


if __name__ == "__main__":

    eletrodomestico = Eletrodomestico1()
    eletrodomestico.set_ligado(True)
    eletrodomestico.imprimir()
