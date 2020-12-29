"""
faça uma função que receba a altura e o raio de um cilindro e retorne
o volume do cilindro.
V = 3.141592 * r ** 2 * altura
"""


def volume_cilindro(raio, altura):
    """
    Calcula o volume do cilindro dado o raio e altura
    :param raio: Valor do raio do cilindro
    :param altura: Valor da altura do cilindro
    :return: Retorna o volume do cilindro
    """
    return f"{3.141592 * raio ** 2 * altura:.2f}"


print(volume_cilindro(5.75, 52.14))
