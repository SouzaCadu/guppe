"""
escreva uma função que compare e retorne verdadeiro, caso uma string seja
anagrama de outra, e falso, caso contrário
"""


def detecta_anagrama(s1, s2):
    """
    Compara e retorna verdadeiro, caso uma string seja
    anagrama de outra, e falso, caso contrário
    :param s1: Qualquer string
    :param s2: Qualquer string
    :return: Verdadeiro, caso uma string seja
             anagrama de outra, e falso, caso contrário
    """

    c1 = [0] * 26
    c2 = [0] * 26

    for i in range(len(s1)):
        pos = ord(s1[i]) - ord('a')
        c1[pos] = c1[pos] + 1

    for i in range(len(s2)):
        pos = ord(s2[i]) - ord('a')
        c2[pos] = c2[pos] + 1

    j = 0
    aindaOK = True
    while j < 26 and aindaOK:
        if c1[j] == c2[j]:
            j = j + 1
        else:
            aindaOK = False

    return aindaOK


print(detecta_anagrama('marrocos', 'socorram'))
print(detecta_anagrama('banana', 'arara'))
