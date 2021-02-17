"""
faça uma função que receba um inteiro N como parâmetro, calcule e retorne
o resultado da seguinte série:
S = 2/4 + 5/5 + 10/6 + ... + (N ** 2 + 1) / (N + 3)
"""


def func_ex_25(num):
    """
    Receba um inteiro N como parâmetro, calcula e retorna
    o resultado da seguinte série:
    S = 2/4 + 5/5 + 10/6 + ... + (N ** 2 + 1) / (N + 3)
    :param num: Número inteiro
    :return: Calculo do resultado da série
    """
    if num <= 0:
        return "Digite um número natural maior que zero!"
    soma = 0
    for i in range(1, num + 1):
        soma += (i ** 2 + 1) / (i + 3)
    return round(soma, 2)


print(func_ex_25(10))
print(func_ex_25(18))
