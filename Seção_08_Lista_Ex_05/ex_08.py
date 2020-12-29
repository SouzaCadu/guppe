"""
sejam A e B os catetos de um triângulo, faça uma função
que calcule a hipotenusa
"""


def pitagoras(cateto_a, cateto_b):
    """
    Calcula o valor da hipotenusa dados os valores de 2 catetos adjacentes
    :param cateto_a: Valor do primeiro cateto
    :param cateto_b: Valor do segundo cateto
    :return: Valor da hipotenusa, dado o teorema de Pitagoras
    """
    return (cateto_a ** 2 + cateto_b ** 2) ** 1 / 2


print(pitagoras(5, 13.9))
