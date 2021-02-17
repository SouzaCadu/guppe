"""
crie um programa contendo as seguintes funções que recebem um vetor V
- Impressão normal do vetor
- Impressão inversa
- Retorna a média aritmética dos elementos do vetor
"""


def imprime_vetor_media(vetor):
    """
    Recebe um vetor V
    - Impressão normal do vetor
    - Impressão inversa
    - Retorna a média aritmética dos elementos do vetor
    :param vetor: Qualquer vetor V com N elementos
    :return: Imprime normalmente o vetor, imprime o vetor inverso, média aritmética
    """
    media = sum(vetor) / len(vetor)
    return print(f"{vetor}, {vetor[::-1]}, {media}")


imprime_vetor_media([-89.748, 1247.78548, 7.15487, 1235, 0.2587, -895.15, 9015])
