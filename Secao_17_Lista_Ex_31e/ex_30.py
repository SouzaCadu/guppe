"""
30) Baseando-se no exercício 29 adicione os métodos fecharPorta e abrirPorta que
deverá mudar o conteúdo do atributo portaFechada conforme o caso.
"""

from ex_29 import Microondas3


class Microondas4(Microondas3):

    def __init__(self):
        super().__init__(porta_fechada=True)

    def fechar_porta(self):
        if self.porta_fechada:
            print("\nA porta do micro ondas já está fechada.")
        else:
            self.set_porta_fechada = True

    def abrir_porta(self):
        if self.porta_fechada:
            self.set_porta_fechada = False
        else:
            print("\nA porta do micro ondas já está aberta.")


if __name__ == "__main__":

    m1 = Microondas4()
    m1.imprimir()
    print("_" * 90, end="\n")
    m1.ligar()
    m1.fechar_porta()
    m1.imprimir()
    print("_" * 90, end="\n")
    m1.desligar()
    m1.abrir_porta()
    m1.imprimir()
    print("_" * 90, end="\n")
    m1.set_porta_fechada = True
    m1.imprimir()
    print("_" * 90, end="\n")
    m1.set_porta_fechada = False
    m1.imprimir()