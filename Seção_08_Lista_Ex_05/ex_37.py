"""
faça uma função não recursiva que receba um número inteiro
positivo N e retorne o hiperfatorial deste número
"""


def hiperfatorial(num):
    """
    Receba um número inteiro positivo N e retorne o hiperfatorial deste número
    :param num: Qualquer número inteiro positivo
    :return: O hiperfatorial deste número
    """
    if num > 0:
        produto = 1
        for i in range(1, num + 1):
            produto *= ((i - 1) ** (i - 1)) * i ** i
        return produto
    return "Digite um número inteiro positivo."


print(hiperfatorial(4))