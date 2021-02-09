"""
faça uma função para verificar se um número é um quadrado perfeito.
"""


def teste_quadrado_perfeito(n):
    """
    Testa se um número é um quadrado perfeito
    :param n: Qualquer número inteiro positivo
    :return:
    """
    if n < 0:
        return f"Insira um número positivo."
    raizq = int(n ** (1 / 2))
    if (raizq ** 2) == n:
        return f"O número {n} é um quadrado perfeito."
    return f"O número {n} não é quadrado perfeito."


print(teste_quadrado_perfeito(91))
print(teste_quadrado_perfeito(100))
