"""
16) Baseando-se no exercício 15 adicione os métodos ligar e deligar que
deverão mudar o conteúdo do atributo ligada conforme o caso.
"""

from ex_15 import Moto6


class Moto7(Moto6):
    def __init__(self):
        super().__init__()
        self._Moto6__ligada = False

    def ligar(self):
        if not self.ligada:
            if self.marcha == self.menor_marcha:
                self._Moto6__ligada = True
                pass
            else:
                print("\nAVISO: A marcha não está no neutro (menor marcha)")
        else:
            print("\nA moto já está ligada.")

    def desligar(self):
        if self.ligada:
            if self.marcha == self.menor_marcha:
                self._Moto6__ligada = False
            else:
                print("\nAVISO: A marcha não está no neutro (menor marcha)")
        else:
            print("\nA moto já está desligada.")

    def imprimir(self):
        print(f"\nMoto modelo: {self.modelo}, marca: {self.marca}, cor: {self.cor}, "
              f"marcha atual: {self.marcha}, a primeira marcha: {self.menor_marcha}, "
              f"última marcha: {self.maior_marcha} e a "
              f"moto está {'ligada' if self._Moto6__ligada else 'desligada'}.")


if __name__ == "__main__":

    honda = Moto7()
    honda.set_marca('Honda')
    honda.set_modelo('GL 1800 Gold Wing Tour')
    honda.set_cor('Vermelha')
    honda.set_marcha(0)
    honda.set_maior_marcha(7)
    honda.set_menor_marcha(0)
    print('=' * 90)
    honda.ligar()
    honda.imprimir()
    print('=' * 90)
    honda.marcha_acima()
    honda.marcha_acima()
    honda.imprimir()
    print('=' * 90)
    honda.marcha_abaixo()
    honda.imprimir()
    print('=' * 90)

    bmw = Moto7()
    bmw.set_marca('BMW')
    bmw.set_modelo('R 1200 S')
    bmw.set_cor('Preta')
    bmw.set_marcha(5)
    bmw.set_maior_marcha(7)
    bmw.set_menor_marcha(0)
    print('=' * 90)
    honda.desligar()
    bmw.imprimir()
    print('=' * 90)
    bmw.marcha_acima()
    bmw.marcha_acima()
    bmw.imprimir()
    print('=' * 90)
    bmw.marcha_abaixo()
    bmw.imprimir()
    print('=' * 90)