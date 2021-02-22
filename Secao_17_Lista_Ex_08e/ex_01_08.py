"""
1) Crie um novo pacote com o nome: heranca. Todas as (três) classes criadas abaixo
deverão ser salvas neste pacote.

2) Crie uma classe Equipamento com dois atributos privados.

3) Crie uma classe Computador com dois atributos sua escolha,
também privados. A classe Computador deverá herdar tudo da classe
Equipamento.

4) Crie os métodos de acesso e de modificação para todos os
atributos definidos em ambas as classes.

5) Crie uma classe TestaEquipamento, que deverá conter o método
main(), crie nela um objeto da classe Equipamento e instancie
os dois atributos que você declarou na classe Equipamento.
Crie também um objeto da classe Computador, utilizando os dois
atributos declarados na própria classe e os dois herdados da classe
Equipamento.

6) O método main() deve exibir as informações dos dois objetos criados.

7) Criar o método exibe() na classe Equipamento para mostrar os dados dessa classe

8) Reescreva o método exibe() na classe Computador, aproveitando o que já
está escrito na superclasse Equipamento
"""


class Equipamento:

    def __init__(self, descricao, preco):
        try:
            if type(descricao) == str:
                if descricao.strip() != "":
                    self.__descricao = descricao
                else:
                    raise ValueError
            else:
                raise ValueError
            if type(preco) != bool:
                if float(preco) >= 0:
                    self.__preco = float(preco)
                else:
                    raise ValueError
            else:
                raise ValueError
        except ValueError:
            print("\nValores inválidos.")
            exit(1)

    @property
    def descricao(self):
        return self.__descricao

    @property
    def preco(self):
        return self.__preco

    @descricao.setter
    def descricao(self, novo_valor):
        try:
            if type(novo_valor) == str:
                if novo_valor.strip() != "":
                    self.__descricao = novo_valor
                else:
                    raise ValueError
            else:
                raise ValueError
        except ValueError:
            print("\nDescrição inválida.")

    @preco.setter
    def preco(self, novo_valor):
        try:
            if type(novo_valor) != bool:
                if float(novo_valor) >= 0:
                    self.__preco = float(novo_valor)
                else:
                    raise ValueError
            else:
                raise ValueError
        except ValueError:
            print("\nPreço inválido.")

    def imprimir(self):
        print(f"\n{self.__descricao} valor {self.__preco}.")


class Computador(Equipamento):

    def __init__(self, descricao, preco, ligado, processador):
        super().__init__(descricao, preco)
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
            if type(processador) == str:
                if processador.strip() != "":
                    self.__processador = processador.strip().title()
                else:
                    raise ValueError
            else:
                raise ValueError
        except ValueError:
            print("\nValores inválidos.")
            exit(1)

    @property
    def ligado(self):
        return self.__ligado

    @property
    def processador(self):
        return self.__processador

    @ligado.setter
    def ligado(self, novo_valor):
        try:
            if type(novo_valor) == str:
                if novo_valor.strip().title() == "False" or novo_valor.strip() == "0":
                    self.__ligado = False
                elif novo_valor.strip().title() == "True" or novo_valor.strip() == "1":
                    self.__ligado = True
                else:
                    raise ValueError
            elif type(novo_valor) == int:
                if novo_valor == 0:
                    self.__ligado = False
                elif novo_valor == 1:
                    self.__ligado = True
                else:
                    raise ValueError
            elif type(novo_valor) == bool:
                self.__ligado = novo_valor
            else:
                raise ValueError
        except ValueError:
            print("\nValor inválido.")

    @processador.setter
    def processador(self, novo_valor):
        try:
            if type(novo_valor) == str:
                if novo_valor.strip() != "":
                    self.__processador = novo_valor.strip().title()
                else:
                    raise ValueError
            else:
                raise ValueError
        except ValueError:
            print("\nProcessador inválido")

    def imprimir(self):
        print(f"\n{self.descricao} valor {self.preco}.")
        print(f"Processador: {self.__processador}")
        print(f"Ligado? {'Sim' if self.ligado else 'Não'}")


class TestaEquipamento:

    def __init__(self):
        pass

    @staticmethod
    def main():
        equipamento = Equipamento("Computador gamer", 13900.00)
        descricao = equipamento.descricao
        preco = equipamento.preco

        computador = Computador(descricao, preco, True, "Core-i9-9940X Skylake")

        print("\nINFORMAÇÕES REFERENTES AO EQUIPAMENTO CRIADO:")
        equipamento.imprimir()

        print("\nINFORMAÇÕES REFERENTES AO COMPUTADOR:")
        computador.imprimir()


if __name__ == "__main__":

    equipamento = Equipamento("Professional Deep Learning Workstation", 11000)
    equipamento.imprimir()

    computador = Computador("ThinkStation P920 Tower Workstation", 32900,
                            False, "Intel Xeon Silver 4110")

    computador.imprimir()

    computador.funcao = " "
    computador.processador = " "

    teste1 = TestaEquipamento()
    teste1.main()


