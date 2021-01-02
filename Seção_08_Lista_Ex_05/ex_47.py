"""
faça um programa que receba uma matriz 4 x 4 e retorne quantos valores maiores que 10 ela possui
"""

from random import randint


def valores_acima_10(matriz):
    """
    Recebe uma matriz 4 x 4 e retorna quantos valores maiores que 10 ela possui
    :param matriz: Qualquer matriz 4 x 4
    :return:  Quantos valores maiores que 10 ela possui
    """
    if len(matriz) != 4:
        return "Insira uma matriz 4 x 4."
    elif len(matriz) == 4:
        for i in range(len(matriz)):
            if len(matriz[i]) != 4:
                return "Insira uma matriz 4 x 4."

    count = 0
    for i in matriz:
        for j in i:
            if j > 10:
                count += 1
    return count


matriz = []
for i in range(4):
    aux = []
    for j in range(4):
        aux.append(randint(1, 100))
    matriz.append(aux)

print(matriz, len(matriz), len(matriz[0]))
print(valores_acima_10(matriz))
