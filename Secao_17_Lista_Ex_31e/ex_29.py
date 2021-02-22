"""
29) Baseando-se no exercício 28 adicione o atributo portaFechada que
deverá ser booleano e deverá indicar se a porta do micro ondas está
ou não fechada. O método imprimir deve ser modificado de forma a mostrar
na tela os valores de todos os métodos.
"""

from ex_28 import Microondas2


class Microondas3(Microondas2):

    def __init__(self, porta_fechada):
        super().__init__()
        self.__porta_fechada = True

    @property
    def porta_fechada(self):
        return self.__porta_fechada

    @porta_fechada.setter
    def set_porta_fechada(self, novo_valor):
        try:
            if type(novo_valor) == str:
                if novo_valor.strip().title() == "False" or novo_valor.strip() == "0":
                    novo_valor = False
                elif novo_valor.strip().title() == "True" or novo_valor.strip() == "1":
                    novo_valor = True
                else:
                    raise ValueError
            elif type(novo_valor) == int:
                if novo_valor == 0:
                    novo_valor = False
                elif novo_valor == 1:
                    novo_valor = True
                else:
                    raise ValueError
            elif type(novo_valor) == bool:
                novo_valor = novo_valor
            else:
                raise ValueError
            if self.__porta_fechada != novo_valor:
                self.__porta_fechada = novo_valor
            else:
                if novo_valor:
                    print("\nA porta do micro ondas está fechada.")
                else:
                    print("\nA porta do micro ondas está aberta.")
        except ValueError:
            print("\nValor inválido.")

    def imprimir(self):
        print(f"O micro ondas está {'ligado.' if self.ligado else 'desligado.'}")
        print(f"Porta fechada: {'Sim' if self.__porta_fechada else 'Não'}")


if __name__ == "__main__":

    m1 = Microondas3(False)
    m1.imprimir()
    print("_" * 90, end="\n")
    m1.ligar()
    m1.imprimir()
    print("_" * 90, end="\n")
    m1.desligar()
    m1.imprimir()
    print("_" * 90, end="\n")
    m1.set_porta_fechada = True
    m1.imprimir()
    print("_" * 90, end="\n")
    m1.set_porta_fechada = False
    m1.imprimir()