"""
8) Baseando-se no exercício 7 adicione um método construtor que permita
a definição de todos os atributos no momento da instanciação do objeto.
"""

from ex_07 import Circulo


class Circulo1(Circulo):

    def __init__(self):
        super().__init__(0.0)


if __name__ == "__main__":
    c2 = Circulo1()
    c2.set_raio(12.98)
    c2.calcular_area()
    c2.calcular_perimetro()
    c2.imprimir()
