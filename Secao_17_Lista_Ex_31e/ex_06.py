"""
6) Baseando-se no exercício 5 adicione um método construtor que
permita a definição de todos os atributos no momento da instanciação
do objeto.
"""

from ex_05 import Retangulo


class Retangulo1(Retangulo):

    def __init__(self):
        super().__init__(0.0, 0.0)


if __name__ == "__main__":

    r2 = Retangulo1()
    r2.set_lado(5, 11)
    r2.calcular_perimetro()
    r2.calcular_area()
    r2.imprimir()
