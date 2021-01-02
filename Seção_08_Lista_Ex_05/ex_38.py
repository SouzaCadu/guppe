"""
faça uma função não recursiva que receba um número inteiro positivo e retorne o fatorial
exponencial desse número.
"""


def fatorial_exponencial(num):
    """
    Recebe um número inteiro positivo e retorne o fatorial
    exponencial desse número.
    :param num: Qualquer número inteiro positivo
    :return: Retorna o fatorial exponencial desse número.
    """
    if num > 0 or num == int(num):
        expoente = num
        while expoente > 1:
            num ^= expoente
            expoente -= 1
            print(num, expoente)
        return num
    return "Digite um número inteiro positivo."


print(fatorial_exponencial(12))
