"""
faça uma função que receba como parâmetro o valor de um ângulo em graus
e calcule o valor do cosseno desse ângulo usando a série de Taylor,
considerar Pi = 3.141593 e n variando de 0 até 5
"""


from math import factorial


def cosseno_serie_taylor(graus, iterador=5):
    """
    Recebe o valor de um ângulo em graus
    e calcula o valor do cosseno usando a série de Taylor
    :param graus:  Qualquer valor de um ângulo em graus
    :param iterador: Número de iterações desejadas para o calculo
    :return: O valor do cosseno usando a série de Taylor
    """
    rad = (graus / 180) * 3.141593
    soma = 0
    for n in range(iterador + 1):
        soma += ((-1) ** n) * (rad ** (2 * n)) / (factorial(2 * n))
    return round(soma, 2)


print(cosseno_serie_taylor(60))
