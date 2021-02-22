"""
27) Baseando-se no exercício 26 adicione um método construtor
que permita o definição de todos os atributos no momento da
instanciação do objeto.
"""

from ex_26 import Microondas


class Microondas1(Microondas):

    def __init__(self):
        super().__init__(ligado=False)


if __name__ == "__main__":

    m1 = Microondas1()
    m1.imprimir()
    print("_" * 90, end="\n")
    m1.set_ligado = True
    m1.imprimir()
    print("_" * 90, end="\n")
    m1.set_ligado = False
    m1.imprimir()
