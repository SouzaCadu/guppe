"""
13) Baseando-se no exercício 12 adicione um método construtor que permita
a definição de todos os atributos no momento da instanciação do objeto.
"""

from ex_12 import Moto3


class Moto4(Moto3):
    def __init__(self):
        super().__init__(maior_marcha=0, menor_marcha=0)


if __name__ == "__main__":

    honda = Moto4()
    honda.set_marca('Honda')
    honda.set_modelo('GL 1800 Gold Wing Tour')
    honda.set_cor('Vermelha')
    honda.set_marcha(5)
    honda.set_maior_marcha(7)
    honda.set_menor_marcha(0)
    honda.imprimir()
    print('=' * 90)
    honda.marcha_acima()
    honda.marcha_acima()
    honda.imprimir()
    print('=' * 90)
    honda.marcha_abaixo()
    honda.imprimir()
    print('=' * 90)
