"""
faça uma função que receba uma matriz 3 x 3
e calcule a soma dos elementos que estão abaixo
da diagonal principal
"""


from random import randint


def soma_abaixo_diagonal_principal(matriz):
    """
    Recebe uma matriz 3 x 3 e calcule a soma dos elementos
    que estão abaixo da diagonal principal
    :param matriz: Qualquer matriz 3 x 3
    :return: Soma dos elementos que estão abaixo da diagonal principal
    """
    soma = 0
    # valida o tamanho da matriz
    if len(matriz) != 3:
        return "Insira uma matriz 3 x 3."
    elif len(matriz) == 3:
        for i in range(len(matriz)):
            if len(matriz[i]) != 3:
                return "Insira uma matriz 3 x 3."

    for i in range(3):
        for j in range(3):
            if i > j:
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
print(soma_abaixo_diagonal_principal(matriz1))
