"""
20) Escreva um código que apresente a classe Televisor, com atributos ligado, canal e volume e, o método imprimir.
O método imprimir deve mostrar na tela os valores de todos os atributos.
O atributo ligado será booleano e deverá indicar o estado atual do televisor, se ligado ou desligado.
O atributo canal deverá indicar o canal atual em que o televisor está sintonizado.
O atributo volume deverá indicar o volume atual do televisor.
"""


class Televisor:

    def __init__(self, canal, volume, ligado):
        self.__canal = int(canal)
        self.__volume = int(volume)
        self.__ligado = ligado

    @property
    def canal(self):
        return self.__canal

    @property
    def volume(self):
        return self.__volume

    @property
    def ligado(self):
        return self.__ligado

    @canal.setter
    def set_canal(self, novo_canal):
        if int(novo_canal) > 0:
            self.__canal = int(novo_canal)

    @volume.setter
    def set_volume(self, novo_valor):
        self.__volume = novo_valor

    @ligado.setter
    def set_ligado(self, novo_valor):
        self.__ligado = novo_valor

    def imprimir(self):
        if self.__ligado:
            print(f"\nO televisor está ligado no canal {self.__canal} no volume {self.__volume}.")
        else:
            print("\nO televisor encontra-se desligado.")


if __name__ == "__main__":

    tv1 = Televisor(9, 10, False)
    tv1.set_ligado = True
    tv1.imprimir()
    print("_" * 90, end="\n")
    tv2 = Televisor(8, 15, False)
    tv2.imprimir()
    print("_" * 90, end="\n")
    tv2.set_ligado = True
    tv2.imprimir()
    print("_" * 90, end="\n")
    tv2.set_volume = 34
    tv2.set_canal = 12
    tv2.imprimir()
