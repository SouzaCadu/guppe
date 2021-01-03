"""
faça uma função que recebe uma matriz A[3][3] e retorna a soma
da diagonal principal e secundária
"""

from random import randint


def soma_diagonais(matriz):
    """
    Recebe uma matriz 3 x 3 e calcule a soma dos elementos
    que estão na diagonal principal e secundária
    :param matriz: Qualquer matriz 3 x 3
    :return: Soma dos elementos que estão na diagonal principal e secundária
    """
    soma_p = 0
    soma_s = 0
    n = 3
    # valida o tamanho da matriz
    if len(matriz) != 3:
        return "Insira uma matriz 3 x 3."
    elif len(matriz) == 3:
        for i in range(len(matriz)):
            if len(matriz[i]) != 3:
                return "Insira uma matriz 3 x 3."

    for i in range(3):
        for j in range(3):
            if i == j:
                soma_p += matriz[i][j]
                # print(f"{soma_p, matriz[i][j]}")

    for i in range(3):
        for j in range(3):
            if i + j == n - 1:
                soma_s += matriz[i][j]
                # print(f"{soma_s, matriz[i][j]}")

    return soma_p, soma_s


matriz1 = []
for i in range(3):
    aux = []
    for j in range(3):
        num = randint(1, 100)
        aux.append(num)
    matriz1.append(aux)

# print(matriz1)
print(soma_diagonais(matriz1))