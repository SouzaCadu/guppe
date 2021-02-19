"""
21) Baseando-se no exercício 20 adicione um método construtor que
permita a definição de todos os atributos no momento da instanciação do
objeto.
"""

from ex_20 import Televisor


class Televisor1(Televisor):

    def __init__(self):
        super().__init__(ligado=False, canal=0, volume=0)


if __name__ == "__main__":

    tv3 = Televisor1()
    tv3.set_ligado(True)
    tv3.set_canal(8)
    tv3.set_volume(15)
    tv3.imprimir()
    print("_" * 90, end="\n")
    tv3.set_ligado(False)
    tv3.imprimir()
