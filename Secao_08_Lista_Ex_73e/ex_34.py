"""
faça uma função não recursiva que receba um número inteiro
positivo ímpar N e retorne o fatorial duplo desse número
"""


def fatorial_duplo(num):
    """
    Função não recursiva que receba um número inteiro
    positivo ímpar N e retorna o fatorial duplo desse número
    :param num:  Qualquer número inteiro positivo ímpar
    :return: O fatorial duplo desse número
    """
    if num % 2 != 0 and num > 0:
        produto = 1
        for i in range(1, num + 1, 2):
            produto *= i
        return produto
    return "Digite um número inteiro ímpar positivo!"


print(fatorial_duplo(75))
