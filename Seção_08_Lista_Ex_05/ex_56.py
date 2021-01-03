"""
faça uma função que recebe uma matriz A[7][6] e uma linha N
e retorne a soma dos elementos dessa linha
"""


from random import randint


def soma_linha_matriz(matriz, linha):
    """
    Recebe uma matriz 7 x 6 e calcule a soma dos elementos
    que estão na linha
    :param matriz: Qualquer matriz 7 x 6
    :param linha: Linha na qual os elementos serão somados
    :return: Soma dos elementos que estão na linha
    """
    soma = 0
    # valida o tamanho da matriz
    if len(matriz) != 7:
        return "Insira uma matriz 3 x 3."
    elif len(matriz) == 7:
        for i in range(len(matriz)):
            if len(matriz[i]) != 6:
                return "Insira uma matriz 3 x 3."

    return sum(matriz[linha])


matriz1 = []
for i in range(7):
    aux = []
    for j in range(6):
        num = randint(1, 100)
        aux.append(num)
    matriz1.append(aux)

print(matriz1)
print(soma_linha_matriz(matriz1, 6))