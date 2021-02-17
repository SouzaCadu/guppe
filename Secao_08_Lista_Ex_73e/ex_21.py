"""
escreva uma função para determinar a quantidade de números primos
abaixo de N
"""


def primos_abaixo_n(num):
    """
    Determina a quantidade de números primos
    abaixo de N
    :param num: Número a ser avaliado
    :return: quantidade de números primos abaixo de N
    """
    if num < 0:
        return "Digite um número natural!"
    qtd = 0
    for i in range(2, num):
        count = 0
        for j in range(1, i + i):
            if i % j == 0:
                count += 1
        if count == 2:
            qtd += 1
    return f"A quantidade de números primos abaixo de {num} é {qtd}."


print(primos_abaixo_n(110))
print(primos_abaixo_n(575))
print(primos_abaixo_n(-5))
