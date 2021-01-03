"""
escreva uma função que retorne a primeira posição de uma
sub-string dentro de uma string. caso não haja nenhuma sub-string retornar -1
"""


def localiza_substring(string, substring):
    """
    Recebe uma string e uma sub-string e retorne a primeira posição da
    sub-string dentro de uma string. Caso não haja nenhuma sub-string retorna -1
    :param string: Qualquer string
    :param substring: Sub-string que se deseja localizar
    :return: Posição da substring, caso não exista -1
    """
    if substring in string:
        string = string.split()
        for sub_s in string:
            if sub_s == substring:
                return sub_s, string.index(substring)
    return -1


print(localiza_substring("Iron Maiden", "Iron"))
print(localiza_substring("Iron Maiden", "Metallica"))