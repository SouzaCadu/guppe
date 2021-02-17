"""
1) Escreva um código que apresente a classe Pessoa, com atributos nome, endereço e telefone e,
o método imprimir. O método imprimir deve mostra todos os valores de todos os atributos.
"""

from Secao_13_Lista_Ex_29e import valida_cadastro


class Pessoa:

    def __init__(self, nome, endereco, telefone):
        if valida_cadastro.valida_nome(nome) and valida_cadastro.valida_endereco(
                endereco) and valida_cadastro.valida_telefone(telefone):
            self.__nome = nome.strip().title()
            self.__endereco = endereco.strip().title()
            self.__telefone = telefone if isinstance(telefone, int) else telefone.strip()
        else:
            print("\nInforme valores válidos.")
            exit(0)

    @property
    def get_nome(self):
        return self.__nome

    @property
    def get_endereco(self):
        return self.__endereco

    @property
    def get_telefone(self):
        return self.__telefone

    def set_nome(self, nome):
        if valida_cadastro.valida_nome(nome):
            self.__nome = nome
        else:
            print("\nNome inválido.")

    def set_endereco(self, endereco):
        if valida_cadastro.valida_endereco(endereco):
            self.__endereco = endereco
        else:
            print(f"\nEndereço inválido.")

    def set_telefone(self, telefone):
        if valida_cadastro.valida_telefone(telefone):
            self.__telefone = telefone
        else:
            print(f"\nTelefone inválido.")

    def imprime_dados(self):
        print(f"Nome: {self.__nome}, endereco: {self.__endereco}, telefone: {self.__telefone}.")


pessoa = Pessoa("Scott Summers", "Nova York - Central Park, 10", "555-1223-9988")
# pessoa.imprime_dados()
