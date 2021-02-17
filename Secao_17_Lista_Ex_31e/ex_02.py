"""
2) Baseando-se no exercício 1 adicione um método construtor que permita a definição
de todos os atributos no momento da instanciação do objeto.
"""

from ex_01 import Pessoa


class Pessoa1(Pessoa):
    def __init__(self):
        super().__init__(" ", " ", " ")


if __name__ == "__main__":

    n1 = Pessoa1()
    n1.set_nome("Warren Worthington III")
    n1.set_telefone("(1) 555-1234-0875")
    n1.set_endereco("5 Avenue, 130, East River, Ny")

    n1.imprime_dados()
