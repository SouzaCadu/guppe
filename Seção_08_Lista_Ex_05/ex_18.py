"""
faça uma função que receba 2 valores, X e Z
e calcule X ** Z
"""


def exponencial(base, potencia):
    """
    Recebe 2 valores, n1 e n2, e calcula n1 ** n2
    :param base: Base da exponenciação
    :param potencia: Potencia que será utilizada
    :return: Exponenciação dos números informados
    """
    return f"{base ** potencia:.2f}"


print(exponencial(2, 10))
print(exponencial(-5, 3.2))
print(exponencial(-7.21, 4.56))