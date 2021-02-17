"""
faça uma função para o cálculo do volume de uma esfere.
"""


def volume_esfera(r):
    """
    Cacula o volume de uma esfera
    :param r: Valor do raio de uma esfera
    :return: Retorna o volume da esfera
    """
    if r < 0:
        return f"Insira um número positivo."
    volume = (4 / 3) * 3.14 * r ** 3
    return f"O volume da esfera é {volume:.2f}."


print(volume_esfera(91))
print(volume_esfera(75.7))
print(volume_esfera(-7))
