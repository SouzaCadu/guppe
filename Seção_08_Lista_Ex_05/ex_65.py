"""
implemente uma função que receba duas strings e um valor
inteiro N. deverão ser concatenados N caracteres da string 2
a string 1 que deve terminar com NULL
"""


def concatena_string(s1, s2, n):
    """
    receba duas strings e um valor inteiro N.
    deverão ser concatenados N caracteres da string 2
    a string 1 que deve terminar com NULL
    :param s1: Qualquer string
    :param s2: Qualquer string
    :param n: Número de caracteres da string 2 que serão
              concatenados na string 1
    :return: Concatena N caracteres da string 2 na string 1
             e finaliza string 1 com NULL
    """
    return s1 + "NULL" + s2[0:n+1]


s1 = "Recebe uma string"
s2 = "Recebe outra string"
n = 2
print(concatena_string(s1, s2, n))
