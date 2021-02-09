"""
elabore um função que receba até 3 notas de um aluno e uma letra,
se a letra for "A" calcule a média simples, se for "P" calcule a
média ponderada por 5, 3 e 2
"""


def calcula_media(n1, n2, n3, tipo="a"):
    """
    Recebe 3 notas e de acordo com o parâmetro tipo calcula
    a média aritmética ou ponderada pelos pesos 5, 3 e 2
    :param n1: Primeira nota
    :param n2: Segunda nota
    :param n3: Terceira nota
    :param tipo: Tipo de média, se for "A" calcula a média simples,
                 se for "P" calcula a média ponderada por 5, 3 e 2
                 por default será calculada a média simples
    :return: Retorna a média das 3 notas de acordo com o parâmetro
    """
    if tipo == "p" or tipo == "P":
        return f"A média ponderada das notas informadas é {(((n1 * 5) + (n2 * 3) + (n3 * 2)) / 10):.2f}"
    return f"A média simples das notas informadas é {(n1 + n2 + n3) / 3:.2f}"


print(calcula_media(8.5, 7, 5))
print(calcula_media(8.5, 6, 7.5, "P"))