"""
faça uma função que receba duas string e retorne a intercalação letra a letra
da primeira com a segunda string. a string intercalada deve ser retornada na primeira string
"""


def intercalar(s1, s2):
    """
    Função que recebe duas string e retorna a intercalação letra a letra
    da primeira com a segunda string
    :param s1: Recebe uma string
    :param s2: Recebe uma string
    :return: Retorna a intercalação letra a letra da primeira com a segunda string.
    Caso não seja uma string, retorna um valor o tipo None
    """

    if type(s1) == str and type(s2) == str:
        inter = ''

        if len(s1) <= len(s2):
            for i in range(len(s1)):
                inter += s1[i] + s2[i]

        else:
            for i in range(len(s2)):
                inter += s1[i] + s2[i]

        return inter


texto1 = "Metallica"
texto2 = "Sepultura"
print(f"{intercalar(texto1, texto2)}")