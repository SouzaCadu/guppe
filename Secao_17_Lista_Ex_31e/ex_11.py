"""
11) Baseando-se no exercício 10 adicione os métodos marchaAcima e
marchaAbaixo que deverão efetuar a troca de marchas, onde o método
marchaAcima deverá subir uma marcha, ou seja, se a moto estiver em
primeira marcha, deverá ser trocada para segunda marcha e assim por diante.
O método marchaAbaixo deverá realizar o oposto, ou seja, descer a marcha.
O método imprimir deve ser modificado de forma a mostrar na tela os valores
de todos os atributos.
"""

from ex_10 import Moto1


class Moto2(Moto1):

    def __init__(self):
        super().__init__()

    def marcha_abaixo(self):
        if self.marcha > 0:
            self._Moto__marcha -= 1
        else:
            print("\nMarcha inválida")

    def marcha_acima(self):
        self._Moto__marcha += 1


if __name__ == "__main__":

    honda = Moto2()
    honda.set_marca('Honda')
    honda.set_modelo('CG125')
    honda.set_cor('Preta')
    honda.set_marcha(8)
    honda.imprimir()
    print('=' * 90)
    honda.marcha_acima()
    honda.marcha_acima()
    honda.imprimir()
    print('=' * 90)
    honda.marcha_abaixo()
    honda.imprimir()
    print('=' * 90)
