"""
7) Escreva um código que apresente a classe Circulo,
com atributos raio, área e perímetro e, os métodos calcularArea,
calcularPerimetro e imprimir. Os métodos calcularArea e calculaPerimetro
devem efetuar seus respectivos cálculos e colocar os valores nos atributos
area e perimetro. O método imprimir deve mostrar na tela os valores de todos
os atributos. Salienta-se que a área de um círculo é obtida pela fórmula
(pi * raio * raio) e o perímetro por (2 * pi * raio), onde pi = 3,141516
"""

from math import pi


class Circulo:

    def __init__(self, raio):
        try:
            if float(raio) >= 0:
                self.__raio = float(raio)
                self.__area = 0.0
                self.__perimetero = 0.0
            else:
                raise ValueError
        except ValueError:
            print("\nValores inválidos")
            exit(1)

    @property
    def raio(self):
        return self.__raio

    @property
    def area(self):
        return self.__area

    @property
    def perimetro(self):
        return self.__perimetero

    def set_raio(self, novo_raio):
        try:
            if float(novo_raio) >= 0:
                self.__raio = float(novo_raio)
                self.__area = 0.0
                self.__perimetero = 0.0
            else:
                raise ValueError
        except ValueError:
            print("\nValores inválidos")
            exit(1)

    def calcular_area(self):
        self.__area = pi * self.__raio ** 2

    def calcular_perimetro(self):
        self.__perimetero = 2 * pi * self.__raio

    def imprimir(self):
        print(f"O círculo tem {self.__raio} de raio, "
              f"{self.__area:.2f} de area e {self.__perimetero:.2f} de perímetro.")


if __name__ == "__main__":

    c1 = Circulo(11.9)
    c1.calcular_area()
    c1.calcular_perimetro()
    c1.imprimir()
