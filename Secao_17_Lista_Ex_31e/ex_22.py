"""
22) Baseando-se no exercicio 21 adicione os métodos ligar e desligar
que deverão mudar o conteúdo do atributo ligado conforme o caso
"""

from ex_21 import Televisor1


class Televisor2(Televisor1):

    def __init__(self):
        super().__init__()
        self._Televisor1__ligado = False

    def ligar(self):
        if not self.__ligado:
            self._Televisor1__ligado = True
        else:
            print("\nTelevisor está desligado.")

    def desligar(self):
        if not self.__ligado:
            pass
        else:
            print("\nTelevisor já está desligado.")


if __name__ == "__main__":

    tv3 = Televisor2()
    tv3.set_ligado(True)
    tv3.set_canal(8)
    tv3.set_volume(15)
    tv3.imprimir()
    print("_" * 90, end="\n")
    tv3.set_ligado(False)
    tv3.imprimir()

