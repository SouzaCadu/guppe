"""
crie uma função que compara duas strings e que retorna se elas
são iguais ou diferentes
"""


def compara_strings(s1, s2):
    """
    compara duas strings e que retorna se elas
    são iguais ou diferentes
    :param s1: Qualquer string
    :param s2: Qualquer string
    :return: Comparação entre elas
    """
    if s1 == s2:
        return "Iguais"
    return "Diferentes"


s1 = "Recebe uma string"
s2 = "Recebe outra string"
print(compara_strings(s1, s2))