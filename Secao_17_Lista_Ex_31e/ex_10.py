"""
10) Baseando-se no exercício 9 adicione um método construtor que permita
a definição de todos os atributos no momento em que o objeto é instanciado
"""

from ex_09 import Moto


class Moto1(Moto):
    def __init__(self):
        super().__init__(marca="", modelo="", cor="", marcha=0)


if __name__ == "__main__":

    moto4 = Moto1()
    moto4.set_modelo("GL 1800 Gold Wing Tour")
    moto4.set_marca("Honda")
    moto4.set_cor("Vermelha")
    moto4.set_marcha(9)
    moto4.imprimir()
