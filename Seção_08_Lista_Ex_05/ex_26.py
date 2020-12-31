"""
faça uma função que receba um número inteiro positivo N
e calcule o somatório de 1 até N
"""


def func_ex_26(num):
    """
    Recebe um número inteiro positivo N
    e calcula o somatório de 1 até N
    :param num: Qualquer número inteiro positivo
    :return: Somatório de 1 até N
    """
    if num <= 0:
        return "Digite um número inteiro positivo maior que zero!"
    soma = [i for i in range(1, num + 1)]
    return sum(soma)


print(func_ex_26(10))
print(func_ex_26(100))
print(func_ex_26(1758))
