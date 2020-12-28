"""
Documentando funções com docstrings

Utilizando usando a propriedade __doc__ podemos acessar
a documentação de uma função

A documentação de uma função pode ser acessada usando o
comando help

"""


def hello_world():
    """
    Uma função que retorna a variável "Hello World"
    :return: "Hello World!"
    """
    return "Hello World!"


print(hello_world())

print(hello_world.__doc__)


def exponencial(base, potencia=2):
    """
    Função que eleva um número a um expoente
    :param base: número que será elevado
    :param potencia: número da potência, default igual 2
    :return: retorna base elevada a potência
    """
    return base ** potencia


print(exponencial(16))

print(exponencial.__doc__)

help(exponencial)