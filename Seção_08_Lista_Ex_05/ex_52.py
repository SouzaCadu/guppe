"""
escreva uma função que receba uma matriz quadrada de ordem N e
calcule a sua transposta
"""


from random import randint


def matriz_transposta(matriz):
    """
    Recebe uma matriz quadrada N e calcule a matriz transposta
    :param matriz: Qualquer matriz quadrada N
    :return: Matriz quadrada N transposta
    """
    return [list(linha) for linha in zip(*matriz)]


matriz1 = []
for i in range(5):
    aux = []
    for j in range(5):
        num = randint(1, 100)
        aux.append(num)
    matriz1.append(aux)

print(matriz1)
print(matriz_transposta(matriz1))
