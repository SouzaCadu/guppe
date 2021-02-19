"""
24) Baseando-se no exercicio 23 adicione os métodos canalAcima e
canalAbaixo, sendo que o método canalAcima deve sintonizar sempre
o próximo canal em relação ao canal atual, onde ao chegar ao maior
canal possível deverá voltar ao canal 1. O método canalAbaixo deve
sintonizar sempre o canal anterior em relação ao canal atual, onde
ao chegar ao canal 1 deverá voltar ao maior canal possível, simulando
desta forma o funcionamento de um televisor.
"""

from ex_23 import Televisor3


class Televisor4(Televisor3):

    def __init__(self):
        super().__init__()
        self._set_qtde_canais = 0
        self._set_vol_maximo = 0
        self.set_volume = 0
        self.set_canal = 1

    def canal_acima(self):
        try:
            if self.get_ligado:
                if 0 >= int(self.set_qtde_canais) or int(self.set_qtde_canais) > int(self.__qtde_canais):
                    raise ValueError
                else:
                    self.set_canal += 1
            else:
                print("\nO televisor está desligado.")
        except ValueError:
            print("\nJá atingiu o máximo de canais exibidos.")
            exit(1)

    def canal_abaixo(self):
        try:
            if self.get_ligado:
                if 0 > int(self.set_qtde_canais) or int(self.set_qtde_canais) > int(self.__qtde_canais):
                    raise ValueError
                else:
                    self.set_canal -= 1
            else:
                print("\nO televisor está desligado.")
        except ValueError:
            print("\nEsse é o primeiro canal exibido.")
            exit(1)


if __name__ == "__main__":

    tv3 = Televisor4()
    tv3.set_ligado(True)
    tv3.set_canal = 8
    tv3.set_volume = 15
    tv3.set_qtde_canais = 10
    tv3.set_vol_maximo = 50
    tv3.imprimir()
    print("_" * 90, end="\n")
    tv3.canal_acima()
    tv3.imprimir()
    print("_" * 90, end="\n")
    tv3.canal_acima()
    tv3.imprimir()
    print("_" * 90, end="\n")
    tv3.canal_acima()
    tv3.imprimir()
    print("_" * 90, end="\n")
    tv3.canal_abaixo()
    tv3.imprimir()
    print("_" * 90, end="\n")
    tv3.set_ligado(False)
    tv3.imprimir()


