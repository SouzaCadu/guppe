"""
15) Baseando-se no exercício 14 adicione um método construtor que
permita a definição de todos os atributos no momento da instanciação do objeto.
"""

from ex_14 import Moto5


class Moto6(Moto5):
    def __init__(self):
        super().__init__(ligada=False)


if __name__ == "__main__":

    honda = Moto6()
    honda.set_marca('Honda')
    honda.set_modelo('GL 1800 Gold Wing Tour')
    honda.set_cor('Vermelha')
    honda.set_marcha(5)
    honda.set_maior_marcha(7)
    honda.set_menor_marcha(0)
    honda.status(True)
    honda.imprimir()
    print('=' * 90)
    honda.marcha_acima()
    honda.marcha_acima()
    honda.imprimir()
    print('=' * 90)
    honda.marcha_abaixo()
    honda.imprimir()
    print('=' * 90)
