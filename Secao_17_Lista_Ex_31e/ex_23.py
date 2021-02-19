"""
23) Baseando-se no exercício 22 adicione os atributos numeroCanais
e, volumeMaximo, onde numeroCanais indica o número máximo de canais
que o televisor pode sintonizar e volumeMaximo indica qual o maior nível
de volume possível. O método imprimir deve ser modificado de forma a mostrar
na tela os valores de todos os atributos.
"""

from ex_22 import Televisor2


class Televisor3(Televisor2):

    def __init__(self, numero_canais, volume_maximo):
        super().__init__()
        self.__numero_canais = int(numero_canais)
        self.__volume_maximo = int(volume_maximo)
        self.set_volume = 0
        self.set_canal = 1

    @property
    def set_numero_canais(self):
        return self.__numero_canais

    @property
    def set_volume_maximo(self):
        return self.__volume_maximo

    def set_canal(self, novo_canal):
        try:
            if self.get_ligado:
                if int(novo_canal) > 0:
                    if int(novo_canal) <= int(self.__numero_canais):
                        self.set_canal = int(novo_canal)
                    else:
                        print(f"\nO televisor já atingiu o número máximo de canais exibidos.")
                else:
                    print("\nO televisor está desligado.")
        except ValueError:
            print("\nValor inválido.")
            exit(1)

    def set_volume(self, novo_volume):
        try:
            if self.get_ligado:
                if int(novo_volume) >= 0:
                    if int(novo_volume) <= int(self.__volume_maximo):
                        self.set_volume = int(novo_volume)
                    else:
                        print("\nO televisor já está no volume máximo.")
                else:
                    print("\nO televisor está desligado.")
        except ValueError:
            print("\nValor inválido.")
            exit(1)

    def imprimir(self):
        print(f"\nO televisor está {'ligado' if self.get_ligado else 'desligado'} "
              f"tem {self.__numero_canais} canais e {self.__volume_maximo} é o volume máximo ")
        if self.get_ligado:
            print(f"e está no canal {self.set_canal} e está no volume {self.set_volume}.")
        else:
            pass


if __name__ == "__main__":

    tv3 = Televisor3(0, 0)
    tv3.set_ligado(True)
    tv3.set_canal = 8
    tv3.set_volume = 32
    tv3.imprimir()
    print("_" * 90, end="\n")
    tv3.set_canal = 11
    tv3.set_volume = 51
    tv3.imprimir()
    print("_" * 90, end="\n")
    tv3.set_ligado(False)
    tv3.imprimir()
