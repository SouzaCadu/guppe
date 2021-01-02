"""
faça uma função que receba um vetor de inteiros e retorne quantos valores
ele possui
"""


def contador_numero_pares(vetor):
    """
    Recebe um vetor de inteiros e retorne quantos valores
    ele possui
    :param vetor:  Vetor de inteiros
    :return: Quantos valores ele possui
    """
    inteiros = 0
    for i in vetor:
        if i == int(i):
            inteiros += 1
    if inteiros == len(vetor):
        count = 0
        for i in vetor:
            if i % 2 == 0:
                count += 1
        return f"O total de valores pares no vetor informado é {count}."


vetor = list(range(30))
print(contador_numero_pares(vetor))
