"""
faça uma função que receba um vetor de reais e retorne a média dele
"""


def media(vetor):
    """
    Receba um vetor de números reais e retorna a média do vetor
    :param vetor: Qualquer vetor de números reais
    :return: Retorna a média do vetor
    """

    return sum(vetor) / len(vetor)


print(f"\n{media([-89.748, 1247.78548, 7.15487, 1235, 0.2587, -895.15, 9015])}")
