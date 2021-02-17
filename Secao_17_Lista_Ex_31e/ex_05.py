"""
5) Escreva um código que apresente a classe Retangulo, com atributos
comprimento, largura, área e perímetro e, os métodos calcularArea,
calcularPerimetro e imprimir. Os métodos calcularArea e calcularPerimetro
devem efetuar seus respectivos cálculos e colocar os valores nos atributos area
e perimetro. O método imprimir deve mostrar na tela os valores de todos os
atributos. Salienta-se que a área de retângulo é obtida peça fórmula (comprimento *
largura) e o perímetro por (2 * comprimento) + (2 * largura)
"""


class Retangulo:

    def __init__(self, largura, comprimento):
        try:
            if float(largura) >= 0:
                if float(comprimento) >= 0:
                    self.__largura = float(largura)
                    self.__comprimento = float(comprimento)
                    self.__area = 0.0
                    self.__perimetero = 0.0
                else:
                    raise ValueError
            else:
                raise ValueError
        except ValueError:
            print("\nValores inválidos")
            exit(1)

    @property
    def largura(self):
        return self.__largura

    @property
    def comprimento(self):
        return self.__comprimento

    @property
    def area(self):
        return self.__area

    @property
    def perimetro(self):
        return self.__perimetero

    def set_lado(self, nova_largura, novo_comprimento):
        try:
            if float(nova_largura) >= 0:
                if float(novo_comprimento) >= 0:
                    self.__largura = float(nova_largura)
                    self.__comprimento = float(novo_comprimento)
                    self.__area = 0.0
                    self.__perimetero = 0.0
                else:
                    raise ValueError
            else:
                raise ValueError
        except ValueError:
            print("\nValores inválidos")
            exit(1)

    def calcular_area(self):
        self.__area = self.__comprimento * self.__largura

    def calcular_perimetro(self):
        self.__perimetero = (self.__comprimento * 2) + (self.__largura * 2)

    def imprimir(self):
        print(f"O retângulo tem {self.__largura} de largura por {self.__comprimento} de comprimento, "
              f"{self.__area:.2f} de area e {self.__perimetero} de perímetro.")


if __name__ == "__main__":

    r1 = Retangulo(4.0, 8.0)
    r1.calcular_area()
    r1.calcular_perimetro()
    r1.imprimir()
