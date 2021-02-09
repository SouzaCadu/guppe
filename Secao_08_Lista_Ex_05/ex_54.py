"""
faça uma função que recebe por parâmetro uma matriz [4][4] e retorna a
soma dos seus elementos
"""


from random import randint


def soma_matriz(matriz):
    """
    Recebe uma matriz 4 x 4 e calcule a soma dos elementos
    :param matriz: Qualquer matriz 4 x 4
    :return: Soma dos elementos
    """
    soma = 0
    # valida o tamanho da matriz
    if len(matriz) != 4:
        return "Insira uma matriz 3 x 3."
    elif len(matriz) == 4:
        for i in range(len(matriz)):
            if len(matriz[i]) != 4:
                return "Insira uma matriz 4 x 4."

    for i in range(4):
        for j in range(4):
            soma += matriz[i][j]
    return soma


matriz1 = []
for i in range(4):
    aux = []
    for j in range(4):
        num = randint(1, 100)
        aux.append(num)
    matriz1.append(aux)

print(matriz1)
print(soma_matriz(matriz1))

