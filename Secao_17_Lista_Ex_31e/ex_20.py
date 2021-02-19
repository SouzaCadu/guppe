"""
20) Escreva um código que apresente a classe Televisor, com atributos
ligado, canal e volume e, o método imprimir. O método imprimir deve
mostrar na tela os valores de todos os atributos. O atributo ligado
será booleano e deverá indicar o estado atual do televisor, se ligado
ou desligado. O atributo canal deverá indicar o canal atual em que
o televisor está sintonizado. O atributo volume deverá indicar o volume
atual do televisor.
"""


class Televisor:

    def __init__(self, ligado, canal, volume):
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
        self.__canal = int(canal)
        self.__volume = int(volume)

    @property
    def get_ligado(self):
        return self.__ligado

    @property
    def get_canal(self):
        return self.__canal

    @property
    def get_volume(self):
        return self.__volume

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
                    print("\nO Televisor já está ligado.")
                else:
                    print("\nO Televisor já está desligado.")
        except ValueError:
            print("\nValor inválido.")

    def set_canal(self, novo_canal):
        try:
            if self.__ligado:
                if int(novo_canal) != bool:
                    if int(novo_canal) > 0:
                        self.__canal = int(novo_canal)
                    else:
                        print("\nCanal inválido")
                else:
                    raise ValueError
            else:
                print("\nO televisor está desligado")
        except ValueError:
            print("\nValor inválido")
            exit(1)

    def set_volume(self, novo_volume):
        try:
            if self.__ligado:
                if int(novo_volume) != bool:
                    if (int(novo_volume) >= 0) and (int(novo_volume) <= 100):
                        self.__volume = int(novo_volume)
                    else:
                        print("\nVolume inválido")
                else:
                    raise ValueError
            else:
                print("\nO televisor está desligado")
        except ValueError:
            print("\nValor inválido")
            exit(1)

    def imprimir(self):
        print(f"\nO televisor está {'ligado' if self.__ligado else 'desligado.'}")
        if self.__ligado:
            print(f"e está no canal {self.__canal} e está no volume {self.__volume}.")
        else:
            pass


if __name__ == "__main__":

    tv1 = Televisor(True, 81, 10)
    tv1.imprimir()
    print("_" * 90, end="\n")
    tv2 = Televisor(False, 81, 10)
    tv2.imprimir()
    print("_" * 90, end="\n")
    tv2.set_ligado(True)
    tv2.set_volume(50)
    tv2.set_canal(34)
    tv2.imprimir()
