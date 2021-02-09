"""
faça uma função "troque" que recebe duas variáveis reais A e B e troca
o valor delas (A recebe o valor de B e B recebe o valor de A)
"""


def troque(var_a, var_b):
    """
    Receba duas variáveis reais A e B e troca
    o valor delas (A recebe o valor de B e B recebe o valor de A)
    :param var_a: Qualquer valor
    :param var_b: Qualquer valor
    :return: var_A recebe o valor de var_b e var_b recebe o valor de var_a
    """
    tupla = (var_a, var_b)
    var_a, var_b = reversed(tupla)
    return f"A = {var_a}, B = {var_b}"


print(troque(15, 25.75))
