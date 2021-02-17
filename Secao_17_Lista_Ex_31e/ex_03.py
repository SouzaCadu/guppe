"""
3) Escreva um código que apresente a classe Quadrado, com atributos lado, área e perímetro e,
os métodos calcularArea, calcularPerimetro e imprimir.
Os métodos calcularArea e calcularPerimetro devem efetuar seus respectivos cálculos e colocar
os valores nos atributos area e perimetro.
O método imprimir deve mostrar na tela os valores de todos os atributos.
Salienta-se que a área de um quadrado é obtida pela fórmula (lado * lado) e o perímetro por (4 * lado).
"""


class Quadrado:

    def __init__(self, lado):
        self.__lado = float(lado)
        self.__area = 0.0
        self.__perimetero = 0.0

    @property
    def lado(self):
        return self.__lado

    @property
    def area(self):
        return self.__area

    @property
    def perimetro(self):
        return self.__perimetero

    def set_lado(self, novo_lado):
        self.__lado = float(novo_lado)
        self.__area = 0.0
        self.__perimetero = 0.0

    def calcular_area(self):
        self.__area = self.__lado ** 2

    def calcular_perimetro(self):
        self.__perimetero = self.__lado * 4

    def imprimir(self):
        print(f"O quadrado tem {self.__lado} de lado, {self.__area:.2f} de area e {self.__perimetero} "
              f"de perímetro.")


if __name__ == "__main__":

    q1 = Quadrado(4.6)
    q1.calcular_area()
    q1.calcular_perimetro()
    q1.imprimir()
