"""
26) Escreva um código que apresente a classe Micro ondas, com atributo
ligado e o método imprimir. O método imprimir deve mostrar na tela os
valores de todos os atributos. O atributo ligado será booleano e verá indicar
o estado atual do micro ondas, se ligado ou desligado.
"""


class Microondas:

    def __init__(self, ligado):
        self.__ligado = ligado

    @property
    def ligado(self):
        return self.__ligado

    @ligado.setter
    def set_ligado(self, novo_valor):
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
            if self.__ligado != novo_valor:
                self.__ligado = novo_valor
            else:
                if novo_valor:
                    print("\nO micro ondas já está ligado.")
                else:
                    print("\nO micro ondas já está desligado")
        except ValueError:
            print("\nValor inválido.")

    def imprimir(self):
        print(f"O micro ondas está {'ligado.' if self.__ligado else 'desligado.'}")


if __name__ == "__main__":

    m1 = Microondas(False)
    m1.imprimir()
    print("_" * 90, end="\n")
    m1.set_ligado = True
    m1.imprimir()
    print("_" * 90, end="\n")
    m1.set_ligado = False
    m1.imprimir()
