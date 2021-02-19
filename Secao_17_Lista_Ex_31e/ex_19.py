"""
19) Baseando-se no exercicio 18 adicione os métodos ligar e desligar
que deverão mudar o conteúdo do atributo ligado conforme o caso.
"""

from ex_18 import Eletrodomestico1


class Eletrodomestico2(Eletrodomestico1):

    def __init__(self):
        super().__init__()
        self._Eletrodomestico1__ligado = bool

    def ligar(self):
        try:
            if not self.ligado:
                self._Eletrodomestico1__ligado = True
                print("\nO eletrodoméstico encontra-se ligado.")
            else:
                print("\nO eletrodoméstico encontra-se desligado.")
        except ValueError:
            print("\nValor inválido.")

    def desligar(self):
        try:
            if not self.ligado:
                self._Eletrodomestico1__ligado = False
                print("\nO eletrodoméstico encontra-se desligado.")
            else:
                print("\nO eletrodoméstico encontra-se ligado.")
        except ValueError:
            print("\nValor inválido.")

    def imprimir(self):
        print(f"\nLigado: {'Sim' if self._Eletrodomestico1__ligado else 'Não'}")


if __name__ == "__main__":

    geladeira = Eletrodomestico2()
    geladeira.imprimir()
    print('=' * 90)
    geladeira.ligar()
    geladeira.imprimir()
    print('=' * 90)
    geladeira.desligar()
    geladeira.imprimir()
    print('=' * 90)
