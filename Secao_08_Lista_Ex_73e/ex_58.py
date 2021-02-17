"""
faça uma função que receba duas matrizes quadradas de ordem N
e retorne uma terceira matriz, como multiplicação das duas
"""

from random import randint


def multiplica_matrizes(matriz_a, matriz_b):
    """
    Recebe duas matrizes quadradas de ordem N
    e retorne uma terceira matriz que é a multiplicação das duas
    :param matriz_a: Qualquer matriz quadrada de ordem N
    :param matriz_b: Qualquer matriz quadrada de ordem N
    :return: Retorna uma terceira matriz que é a multiplicação das duas
    """
    # valida se é uma matriz quadrada
    for i in range(len(matriz_a)):
        for j in range(len(matriz_a[i])):
            if not(len(matriz_a) == len(matriz_a[i])):
                return "Insira uma matriz quadrada."

    for i in range(len(matriz_b)):
        for j in range(len(matriz_b[i])):
            if not(len(matriz_b) == len(matriz_b[i])):
                return "Insira uma matriz quadrada."

    matriz_c = []
    for i in range(len(matriz_a)):
        aux1 = []
        for j in range(len(matriz_a)):
            aux1.append(matriz_a[i][j] * matriz_b[i][j])
            # print(matriz_c, aux1, matriz_a[i][j], matriz_b[i][j])
        matriz_c.append(aux1)

    return matriz_c


matriz1 = []
for i in range(2):
    aux = []
    for j in range(2):
        num = randint(1, 100)
        aux.append(num)
    matriz1.append(aux)

matriz2 = []
for i in range(2):
    aux = []
    for j in range(2):
        num = randint(1, 100)
        aux.append(num)
    matriz2.append(aux)


print(matriz1, matriz2)
print(multiplica_matrizes(matriz1, matriz2))
