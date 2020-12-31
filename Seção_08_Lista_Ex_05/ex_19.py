"""
faça uma função que retorne o maior fator primo de um número
"""


def maior_fator_primo(num):
    """
    Retorne o maior fator primo de um número
    :param num: Qualquer número inteiro
    :return: O maior fator primo de um número
    """
    if num == 1:
        return 1
    elif num <= 0:
        return "Digite um número natural."
    fp = 2  # Nota: fp = fator primo
    while num != 1:
        if num % fp == 0:
            num = num / fp
        else:
            fp += 1
    return fp


print(maior_fator_primo(2))
print(maior_fator_primo(100))
print(maior_fator_primo(360))
