"""
faça uma função que recebe 2 vetores de 10 números inteiros e
crie um terceiro vetor que calcule e retorne união dos dois primeiros
"""

from random import randint


def uniao_vetores(vetor_a, vetor_b):
    """
    Receba 2 vetores de 10 números inteiros e
    calcule e retorne um terceiro vetor união dos dois primeiros
    :param vetor_a: Qualquer vetor de 10 números inteiros
    :param vetor_b: Qualquer vetor de 10 números inteiros
    :return: Um terceiro vetor que é união dos dois primeiros
    """
    # valida o tamanho dos vetores
    if len(vetor_a) != 10:
        return "Insira um vetor com 10 elementos."
    elif len(vetor_a) == 10:
        for i in vetor_a:
            if i != int(i):
                return "O vetor deve conter apenas números inteiros."

    if len(vetor_b) != 10:
        return "Insira um vetor com 10 elementos."
    elif len(vetor_b) == 10:
        for i in vetor_b:
            if i != int(i):
                return "O vetor deve conter apenas números inteiros."

    vetor_c = []
    for i in range(10):
        vetor_c.append(vetor_a[i])
        vetor_c.append(vetor_b[i])
    return vetor_c


matriz1 = []
matriz2 = []
for i in range(10):
    num1 = randint(1, 100)
    num2 = randint(1, 100)
    matriz1.append(num1)
    matriz2.append(num2)

print(matriz1, matriz2)
print(uniao_vetores(matriz1, matriz2))
