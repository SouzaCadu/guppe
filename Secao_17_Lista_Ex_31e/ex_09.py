"""
9) Escreva um código que apresente a classe Moto, com
atributos marca, modelo, cor e marcha e, o método imprimir. O método
imprimir deve mostrar na tela os valores de todos os atributos. O
atributos marcha indica em que a marcha a Moto se encontra no momento, sendo
representado de forma inteira, onde 0 - neutro, 1 - primeira, 2 - segunda, etc.
"""

from Secao_13_Lista_Ex_29e import valida_cadastro


class Moto:

    def __init__(self, marca, modelo, cor, marcha):
        self.__marca = marca
        self.__modelo = modelo
        try:
            if valida_cadastro.valida_nome(marca):
                self.__cor = cor
            else:
                raise ValueError
        except ValueError:
            print("\nValores inválidos")
            exit(1)
        try:
            if int(marcha) < 0:
                raise ValueError
            else:
                self.__marcha = marcha
        except ValueError:
            print("\nValores inválidos")
            exit(1)

    @property
    def marca(self):
        return self.__marca

    @property
    def modelo(self):
        return self.__modelo

    @property
    def cor(self):
        return self.__cor

    @property
    def marcha(self):
        return self.__marcha

    def set_marca(self, nova_marca):
        try:
            if type(nova_marca) == str:
                if self.__marca.strip() == "":
                    self.__marca = nova_marca.strip().title()
                else:
                    print("\nMarca já existe.")
            else:
                raise ValueError
        except ValueError:
            print("\nMarca inválida.")

    def set_modelo(self, novo_modelo):
        try:
            if type(novo_modelo) == str:
                if self.__modelo.strip() == "":
                    self.__modelo = novo_modelo.strip().title()
                else:
                    print("\nModelo já existe.")
            else:
                raise ValueError
        except ValueError:
            print("\nModelo inválido.")

    def set_cor(self, nova_cor):
        try:
            if type(nova_cor) == str and valida_cadastro.valida_nome(nova_cor):
                if self.__cor.strip() == "":
                    self.__cor = nova_cor.strip().title()
                else:
                    print("\nCor já cadastrada.")
            else:
                raise ValueError
        except ValueError:
            print("\nCor inválida.")

    def set_marcha(self, nova_marcha):
        try:
            if int(nova_marcha) >= 0:
                self.__marcha = int(nova_marcha)
            else:
                raise ValueError
        except ValueError:
            print("\nValor inválido")

    def imprimir(self):
        print(f"\nMoto modelo: {self.modelo}, marca: {self.marca}, cor: {self.cor}, "
              f"marcha atual: {self.marcha}")


if __name__ == "__main__":

    moto1 = Moto("BMW", "K 1600 GTL", "Preta", 8)
    moto1.imprimir()

    moto2 = Moto("BMW", "S 1000 RR", "Prata", 8)
    moto2.imprimir()

    moto3 = Moto("Suzuki", "Hayabusa", "Cinza", 8)
    moto3.imprimir()
