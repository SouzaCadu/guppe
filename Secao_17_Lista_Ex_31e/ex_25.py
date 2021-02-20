"""
25) Baseando-se no exercício 24 adicione os métodos volumeAcima
e volumeAbaixo, sendo que o método volumeAcima deve modificar
o volume para o próximo nível de volume possível, onde ao chegar
ao volumeMaximo não poderá possibilitar que o volume seja alterado.
O método volumeAbaixo deve modificar o volume para o nível imediatamente
inferior de volume me relação ao volume atual, não podendo ser menor do
que 0, simulando desta forma o funcionamento de um televisor.
"""

from ex_24 import Televisor4


class Televisor5(Televisor4):

    def __init__(self):
        super().__init__()

    def volume_acima(self):
        if self.set_volume == self.set_vol_maximo:
            print("A televisão está no volume máximo.")
        else:
            self.set_volume += 1

    def volume_abaixo(self):
        if self.set_volume == 0:
            print("A televisão está no mudo.")
        else:
            self.set_volume -= 1


if __name__ == "__main__":

    tv3 = Televisor5()
    tv3.set_num_canal = 15
    tv3.set_vol_maximo = 15
    tv3.ligar()
    tv3.set_canal = 10
    tv3.set_volume = 10
    tv3.imprimir()
    print("_" * 90, end="\n")
    [tv3.volume_acima() for _ in range(10)]
    tv3.imprimir()
    print("_" * 90, end="\n")
    [tv3.volume_abaixo() for _ in range(16)]
    tv3.imprimir()
    print("_" * 90, end="\n")
