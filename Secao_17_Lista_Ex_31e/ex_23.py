"""
23) Baseando-se no exercício 22 adicione os atributos numeroCanais e volumeMaximo.
Onde numeroCanais indica o número máximo de canais que o televisor pode sintonizar e
volumeMaximo indica qual o maior nível de volume possível.
O método imprimir deve ser modificado de forma a mostrar
na tela os valores de todos os atributos.
"""

from ex_22 import Televisor2


class Televisor3(Televisor2):

    def __init__(self, numero_canais, volume_maximo):
        super().__init__()
        self.__numero_canais = int(numero_canais)
        self.__volume_maximo = int(volume_maximo)

    @property
    def numero_canais(self):
        return self.__numero_canais

    @property
    def volume_maximo(self):
        return self.__volume_maximo

    @numero_canais.setter
    def set_num_canal(self, novo_valor):
        if int(novo_valor) > 0:
            if int(novo_valor) == int(self.__numero_canais):
                print("O televisor já está exibindo o máximo de canais")
            else:
                self.__numero_canais = int(novo_valor)

    @volume_maximo.setter
    def set_vol_maximo(self, novo_valor):
        if int(novo_valor) > 0:
            if int(novo_valor) == int(self.__volume_maximo):
                print("O televisor já está no volume máximo.")
            else:
                self.__volume_maximo = int(novo_valor)

    def imprimir(self):
        if self._Televisor2__set_ligado:
            print(f"\nO televisor tem {self.__numero_canais} canais, o volume máximo é {self.__volume_maximo}"
                  f" e está ligado no canal {self.canal} no volume {self.volume}.")
        else:
            print("\nO televisor encontra-se desligado.")


if __name__ == "__main__":

    tv3 = Televisor3(10, 35)
    tv3.set_canal = 8
    tv3.set_volume = 32
    tv3.ligar()
    tv3.imprimir()
    print("_" * 90, end="\n")
    tv3.desligar()
    tv3.imprimir()
    print("_" * 90, end="\n")
    tv3.ligar()
    tv3.set_vol_maximo = 50
    tv3.set_num_canal = 110
    tv3.imprimir()
    print("_" * 90, end="\n")
    tv3.set_vol_maximo = 50
    tv3.set_num_canal = 110
    tv3.imprimir()

