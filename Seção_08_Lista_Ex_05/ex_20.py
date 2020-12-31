"""
faça uma função que receba um número inteiro positivo N
e calcule o seu fatorial N!
"""


def fatorial(num):
    """
    Recebe um número inteiro positivo e calcule o seu fatorial
    :param num: Número positivo
    :return: Fatorial do número informado
    """
    i = 1  # contador
    n_fat = 1
    if num <= 0:
        return "Digite um número natural"
    # calcule n!
    while i <= int(num):
        n_fat = n_fat * i
        i = i + 1
    return n_fat


print(fatorial(2))
print(fatorial(4))
print(fatorial(-4))
