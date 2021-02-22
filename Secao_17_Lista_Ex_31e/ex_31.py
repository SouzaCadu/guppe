"""
31) Baseando-se no exercício 30 modifique o método ligar para que só ligue o equipamento quando a porta
do mesmo estiver fechada, simulando assim o funcionamento de um micro ondas.
"""

from ex_30 import Microondas4

class Microondas5(Microondas4):

    def __init__(self):
        super().__init__()

    def ligar(self):
        if self.porta_fechada:
            if self.set_ligado:
                print("\nO micro ondas já está ligado.")
            else:
                self.set_ligado = True
        else:
            print("\nA porta do micro ondas está aberta.")


if __name__ == "__main__":
    m1 = Microondas5()
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
