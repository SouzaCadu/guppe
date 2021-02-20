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
        super().__init__(numero_canais=0, volume_maximo=0)

    def canal_acima(self):
        if self.set_canal == self.set_num_canal:
            self.set_canal = 1
        else:
            self.set_canal += 1

    def canal_abaixo(self):
        if self.set_canal == 1:
            self.set_canal = self.set_num_canal
        else:
            self.set_canal -= 1


if __name__ == "__main__":

    tv3 = Televisor4()
    tv3.set_num_canal = 15
    tv3.set_vol_maximo = 15
    tv3.ligar()
    tv3.set_canal = 10
    tv3.set_volume = 10
    tv3.imprimir()
    print("_" * 90, end="\n")
    [tv3.canal_acima() for _ in range(10)]
    tv3.imprimir()
    print("_" * 90, end="\n")
    [tv3.canal_abaixo() for _ in range(10)]
    tv3.imprimir()
    print("_" * 90, end="\n")