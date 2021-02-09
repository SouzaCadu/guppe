"""
faça uma função que receba dois números inteiros positivos e retorne a
soma dos N números inteiros existentes entre eles
"""


def soma_intervalo(n1, n2):
    """
    Recebe dois números inteiros positivos e retorne a
    soma dos N números inteiros existentes entre eles
    :param n1: Primeiro número
    :param n2: Segundo número
    :return: Retorna a soma dos N números existentes entre eles
    """
    soma = 0
    if n1 < n2 and n1 <= 0 or n2 <= 0:
        return f"Intervalo inválido!"
    else:
        for i in range(n1, n2 + 1):
            soma += i
    return soma


print(soma_intervalo(1, 10))
print(soma_intervalo(0, 55))
print(soma_intervalo(-1, 55))
