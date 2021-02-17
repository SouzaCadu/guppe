"""
faça uma função que receba uma matriz 3 x 3 e calcule e retorne a soma
dos elementos que estão na diagonal secundária
"""

from random import randint


def soma_diagonal_secundaria(matriz):
    """
    Recebe uma matriz 3 x 3 e calcule a soma dos elementos
    que estão na diagonal secundária
    :param matriz: Qualquer matriz 3 x 3
    :return: Soma dos elementos que estão na diagonal secundária
    """
    soma = 0
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
            if i + j == n - 1:
                soma += matriz[i][j]
                # print(f"{soma, matriz[i][j]}")
    return soma


matriz1 = []
for i in range(3):
    aux = []
    for j in range(3):
        num = randint(1, 100)
        aux.append(num)
    matriz1.append(aux)

# print(matriz1)
print(soma_diagonal_secundaria(matriz1))
