"""
faça uma função que receba como parâmetro o valor de um ângulo em graus
e calcule o valor do seno usando a série de Taylor
sin(x) = Somatório (-1) ** n / (2n + 1) ^ x ^ 2n + 1
onde x é o valor do ângulo em raianos, considerar Pi = 3.141593
e n variando de 0 até 5
"""

from math import factorial


def seno_serie_taylor(graus, iterador=5):
    """
    Recebe o valor de um ângulo em graus
    e calcula o valor do seno usando a série de Taylor
    :param graus:  Qualquer valor de um ângulo em graus
    :param iterador: Número de iterações desejadas para o calculo
    :return: O valor do seno usando a série de Taylor
    """
    # transforma o ângulo em graus para radianos
    rad = (graus / 180) * 3.141593
    soma = 0
    for n in range(iterador + 1):
        soma += ((-1) ** n) * (rad ** (2 * n + 1))/(factorial(2 * n + 1))
    return round(soma, 2)


print(seno_serie_taylor(30))
