"""
faça uma função que receba um vetor de inteiros e retorne o maior valor
"""


def maior_numero(vetor):
    """
    Receba um vetor de inteiro e retorna o maior valor
    :param vetor: Qualquer vetor de números inteiros
    :return: Retorna o maior valor
    """

    inteiros = 0
    for i in vetor:
        if i == int(i):
            inteiros += 1

    if inteiros == len(vetor):
        return max(vetor)


print(f"\nMaior valor: {maior_numero([3782, 7455, 852147, 13258, 98548, 652378, 8521479, 985647, 7548987, 12357489])}")
print(f"\nMaior valor: {maior_numero(list(range(150)))}")
