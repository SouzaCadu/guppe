"""
faça uma função que calcule o desvio de um vetor V contendo N números
"""


def desvio_padrao(vetor):
    """
    Calcula o desvio de um vetor V contendo N números
    :param vetor: Qualquer vetor V com N elementos
    :return: Desvio padrão do vetor
    """
    media = sum(vetor) / len(vetor)
    variancia = 0
    for i in vetor:
        variancia += (i - media) ** 2
    return (variancia / len(vetor) - 1) ** 0.5


print(f"\n{desvio_padrao([-89.748, 1247.78548, 7.15487, 1235, 0.2587, -895.15, 9015])}")
