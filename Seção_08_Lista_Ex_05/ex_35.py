"""
faça uma função não recursiva que receba u número inteiro positivo
N e retorne o fatorial quádruplo desse número
"""


from math import factorial


def fatorial_quadruplo(num):
    """
    Função não recursiva que recebe um número inteiro positivo
    N e retorne o fatorial quádruplo desse número
    :param num: Qualquer número inteiro positivo
    :return: O fatorial quádruplo desse número
    """
    if num >= 0:
        return factorial(2 * num) / factorial(num)
    return "Digite um número inteiro positivo."


print(fatorial_quadruplo(9))
