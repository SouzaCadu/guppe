"""
faça uma função que receba 2 números e retorne qual deles é o maior
"""


def maior_valor(v1, v2):
    """
    Função que recebe 2 números e retorne qual deles é o maior
    :param v1: Primeiro valor
    :param v2: Segundo valor
    :return: Qual deles é o maior
    """
    if v1 > v2:
        return f"O maior valor é {v1}."
    return f"O maior valor é {v2}."


print(maior_valor(12, 58.9))
print(maior_valor(89.7, 38.9))
