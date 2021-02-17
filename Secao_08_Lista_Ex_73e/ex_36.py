"""
faça uma função não recursiva que receba um número inteiro positivo N
e retorne o superfatorial desse número.
"""

from math import factorial

def superfatorial(num):
    """
    Recebe um número inteiro positivo N
    e retorne o superfatorial desse número.
    :param num: Qualquer número inteiro positivo
    :return: O superfatorial desse número.
    """
    if num > 0:
        spf = 1
        for i in range(1, num + 1):
            spf *= factorial(i)
        return spf
    return "Digite um número inteiro positivo."


print(superfatorial(4))
