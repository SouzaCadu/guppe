"""
4) Baseando-se no exercício 3 adicione um método construtor que permita a definição de todos os
atributos no momento da instanciação do objeto.
"""

from ex_03 import Quadrado


class Quadrado1(Quadrado):
    def __init__(self):
        super().__init__(0.0)


if __name__ == "__main__":

    q2 = Quadrado1()
    q2.set_lado(5)
    q2.calcular_perimetro()
    q2.calcular_area()
    q2.imprimir()
