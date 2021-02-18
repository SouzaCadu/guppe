"""
17) Escreva um código que apresente a classe Eletrodoméstico, com atributo
ligado e o método imprimir. O método imprimir deve mostrar na tela os valores de
todos os atributos. O atributo ligado será booleano e deverá indica o estado
atual do eletrodoméstico, se ligado ou desligado.
"""


class Eletrodomestico:

    def __init__(self, ligado):
        try:
            if type(ligado) == str:
                if ligado.strip().title() == "False" or ligado.strip() == "0":
                    self.__ligado = False
                elif ligado.strip().title() == "True" or ligado.strip() == "1":
                    self.__ligado = True
                else:
                    raise ValueError
            elif type(ligado) == int:
                if ligado == 0:
                    self.__ligado = False
                elif ligado == 1:
                    self.__ligado = True
                else:
                    raise ValueError
            elif type(ligado) == bool:
                self.__ligado = ligado
            else:
                raise ValueError
        except ValueError:
            print("\nValor inválido.")
            exit(1)

    @property
    def ligado(self):
        return self.__ligado

    def set_ligado(self, status):
        try:
            if type(status) == str:
                if status.strip().title() == "False" or status.strip() == "0":
                    status = False
                elif status.strip().title() == "True" or status.strip() == "1":
                    status = True
                else:
                    raise ValueError
            elif type(status) == int:
                if status == 0:
                    status = False
                elif status == 1:
                    status = True
                else:
                    raise ValueError
            elif type(status) == bool:
                status = status
            else:
                raise ValueError
            if self.__ligado != status:
                self.__ligado = status
            else:
                if status:
                    print("\nO eletrodoméstico encontra-se ligado.")
                else:
                    print("\nO eletrodoméstico encontra-se desligado.")
        except ValueError:
            print("\nValor inválido.")

    def imprimir(self):
        print(f"\nLigado: {'Sim' if self.__ligado else 'Não'}")


if __name__ == "__main__":

    geladeira = Eletrodomestico(False)
    geladeira.imprimir()
    print('=' * 90)
    geladeira.set_ligado(True)
    geladeira.imprimir()
    print('=' * 90)
    geladeira.set_ligado(False)
    geladeira.imprimir()
    print('=' * 90)
