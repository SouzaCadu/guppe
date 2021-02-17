"""
faça uma função que verifica se uma matriz quadrada de ordem N é a matriz identidade
"""

from random import randint


def valida_matriz_identidade(matriz):
    """
    Receba uma matriz quadrada de ordem N e verifica se é uma matriz identidade
    :param matriz: Qualquer matriz quadrada de ordem N
    :return: Retorna um valor True, caso seja uma matriz identidade, do contrário retorna False
    """
    # valida se é uma matriz quadrada
    quadrada = True
    for i in range(len(matriz)):
        for j in range(len(matriz[i])):
            if not(len(matriz) == len(matriz[i])):
                return "Insira uma matriz quadrada"

    if quadrada:
        diagonal1 = True
        resto0 = True
        for i in range(len(matriz)):
            for j in range(len(matriz[i])):
                if i == j and not(matriz[i][j] == 1):
                    diagonal1 = False
                if not(i == j) and not(matriz[i][j] == 0):
                    resto0 = False
        if diagonal1 and resto0:
            return True
        return False
    return False


matriz = [[1, 0, 0], [0, 1, 0], [0, 0, 1]]
print(valida_matriz_identidade(matriz))

matriz1 = []
for i in range(5):
    aux = []
    for j in range(5):
        num = randint(1, 100)
        aux.append(num)
    matriz1.append(aux)

print(matriz1)
print(valida_matriz_identidade(matriz1))
