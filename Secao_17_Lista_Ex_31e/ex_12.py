"""
12) Baseando-se no exercicio 11 adicione os atributos menorMarcha
e maiorMarcha, onde o atributo menorMarcha indica qual será a menor
marcha possível para a moto e o atributo maiorMarcha indica qual será
a maior marcha possível. Desta forma os métodos marchaAcima e marchaAbaixo
deve ser reescritos de forma a não permitirem a troca de marchar para valores
abaixo da menorMarcha e acima da maiorMarcha. O método imprimir deve ser
modificado de forma a mostrar na tela os valores de todos os atributos.
"""

from ex_11 import Moto2


class Moto3(Moto2):

    def __init__(self, menor_marcha, maior_marcha):
        super().__init__()
        self._Moto__marcha = 0
        try:
            if int(menor_marcha) >= 0 and int(maior_marcha >= 0):
                self.__menor_marcha = int(menor_marcha)
                self.__maior_marcha = int(maior_marcha)
            else:
                raise ValueError
        except ValueError:
            print("\nValores inválidos")
            exit(1)

    @property
    def menor_marcha(self):
        return self.__menor_marcha

    @property
    def maior_marcha(self):
        return self.__maior_marcha

    def set_maior_marcha(self, ultima_marcha):
        try:
            if self.__maior_marcha == 0:
                if int(ultima_marcha) > 0 and int(ultima_marcha) >= self.marcha:
                    self.__maior_marcha = int(ultima_marcha)
                else:
                    raise ValueError
            else:
                print("\nMaior marcha já definida.")
        except ValueError:
            print("\nValor inválido.")

    def set_menor_marcha(self, primeira_marcha):
        try:
            if primeira_marcha == 0:
                if int(primeira_marcha) <= int(self.maior_marcha):
                    self.__menor_marcha = int(primeira_marcha)
                else:
                    raise ValueError
            else:
                print("\nPrimeira marcha já definida.")
        except ValueError:
            print("\nValor inválido.")

    def marcha_abaixo(self):
        if self.marcha > self.__menor_marcha:
            self._Moto__marcha -= 1
        else:
            print("\nJá se encontra na primeira marcha")

    def marcha_acima(self):
        if self.marcha < self.__maior_marcha:
            self._Moto__marcha += 1
        else:
            print("\nJá se encontra na última marcha")

    def imprimir(self):
        print(f"\nMoto modelo: {self.modelo}, marca: {self.marca}, cor: {self.cor}, "
              f"marcha atual: {self.marcha}, a primeira marcha: {self.__menor_marcha}, "
              f"última marcha: {self.__maior_marcha}")


if __name__ == "__main__":

    honda = Moto3(0, 7)
    honda.set_marca('Honda')
    honda.set_modelo('GL 1800 Gold Wing Tour')
    honda.set_cor('Vermelha')
    honda.set_marcha(5)
    honda.imprimir()
    print('=' * 90)
    honda.marcha_acima()
    honda.marcha_acima()
    honda.imprimir()
    print('=' * 90)
    honda.marcha_abaixo()
    honda.imprimir()
    print('=' * 90)

