"""
14)Baseando-se no exercício 13 adicione o atributo ligada que terá a função
de indicar se a moto está ligada ou não. Este atributo deverá ser do tipo
booleano. O método imprimir deve ser modificado de forma a mostrar na tela
os valores de todos os atributos.
"""

from ex_13 import Moto4


class Moto5(Moto4):

    def __init__(self, ligada):
        super().__init__()
        self.__ligada = False

    @property
    def ligada(self):
        return self.__ligada

    def set_ligada(self, ligada):
        if ligada:
            self.__ligada = True
        else:
            self.__ligada = False
            self._Moto__marcha = 0

    def marcha_abaixo(self):
        if self.__ligada:
            pass
            if self.marcha > self.menor_marcha:
                self._Moto__marcha -= 1
            else:
                print(f"\nJá se encontra na primeira marcha")

    def marcha_acima(self):
        if self.__ligada:
            pass
            if self.marcha < self.maior_marcha:
                self._Moto__marcha += 1
            else:
                print("\nJá se encontra na última marcha")

    def imprimir(self):
        print(f"\nMoto modelo: {self.modelo}, marca: {self.marca}, cor: {self.cor}, "
              f"marcha atual: {self.marcha}, a primeira marcha: {self.menor_marcha}, "
              f"última marcha: {self.maior_marcha} e a "
              f"moto está {'ligada' if self.ligada else 'desligada'}.")


if __name__ == "__main__":

    honda = Moto5(False)
    honda.set_marca('Honda')
    honda.set_modelo('GL 1800 Gold Wing Tour')
    honda.set_cor('Vermelha')
    honda.set_marcha(2)
    honda.set_maior_marcha(7)
    honda.set_menor_marcha(0)
    honda.set_ligada(True)
    honda.imprimir()
    print('=' * 90)
    honda.marcha_acima()
    honda.marcha_acima()
    honda.imprimir()
    print('=' * 90)
    honda.marcha_abaixo()
    honda.imprimir()
    print('=' * 90)

    bmw = Moto5(False)
    bmw.set_marca('BMW')
    bmw.set_modelo('R 1200 S')
    bmw.set_cor('Preta')
    bmw.set_marcha(3)
    bmw.set_maior_marcha(7)
    bmw.set_menor_marcha(0)
    bmw.set_ligada(False)
    bmw.imprimir()
    print('=' * 90)
    bmw.marcha_acima()
    bmw.marcha_acima()
    bmw.imprimir()
    print('=' * 90)
    bmw.marcha_abaixo()
    bmw.imprimir()
    print('=' * 90)