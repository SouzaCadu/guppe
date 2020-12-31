"""
faça uma função para calcular o número neperiano usando uma série
a função deve ter como parâmetro o número de termos que serão somados
"""


from math import factorial


def numero_neperiano(num):
    """
    Recebe um número e calcula o número neperiano usando uma série
    :param num: Qualquer número
    :return: Número neperiano usando uma série
    """
    soma = 0
    for i in range(num + 1):
        soma += 1 / factorial(i)
    return soma


print(numero_neperiano(1000))
