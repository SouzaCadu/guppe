"""
1) Crie uma classe para representar uma pessoa, como os atributos privados de nome, idade e altura.
Crie os métodos públicos necessários para sets e gets e também um método para imprimir os dados de
uma pessoa.
"""


class Pessoa:

    def __init__(self, nome, idade, altura) -> object:
        """
        Classe pessoa
        :param nome: string com o nome da pessoa
        :param idade: inteiro com o valor da idade
        :param altura: float com a altura em metros
        """
        self.__nome = str(nome)
        self.__idade = int(idade)
        self.__altura = float(altura)

    def get_nome(self):
        return self.__nome

    def get_idade(self):
        return self.__idade

    def get_altura(self):
        return self.__altura

    def set_nome(self, nome):
        self.__nome = nome

    def set_idade(self, idade):
        self.__idade = idade

    def set_altura(self, altura):
        self.__altura = altura

    def imprime_dados(self):
        print(f"Nome: {self.__nome}, idade: {self.__idade}, altura: {self.__altura}.")


p1 = Pessoa("Tony Stark", 34, 1.87)
# p1.imprime_dados()
