"""
faça uma função para verificar se um número é positivo ou negativo.
deve ser retornado 1 se positivo, -1 se negativo e 0 for igual a 0.
"""


def teste_positivo_negativo(n):
    """
    Verifica se um nome é positivo ou negativo
    :param n: Qualquer número real
    :return: Se o valor for positivo retorna 1,
             se negativo retorna -1, se 0 retorna 0
    """
    if n > 0:
        return 1
    elif n < 0:
        return -1
    return 0


print(teste_positivo_negativo(25.8))
print(teste_positivo_negativo(-75.2))
print(teste_positivo_negativo(0))
