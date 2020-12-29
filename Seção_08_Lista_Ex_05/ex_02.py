"""
faça uma função que receba a data atual (dia, mês, ano) como inteiro
e exiba como texto por extenso
"""


def data_extenso(data):
    """
    Recebe uma string contendo uma data no formato dd/mm/aaaa
    e retorna essa data por extenso
    :param data: Uma string contendo a data no formato dd/mm/aaaa
    :return: Retorna a data com o mês por extenso
    """
    dia, mes, ano = data.split("/")
    if mes == 1:
        mes_extenso = "janeiro"
    elif mes == 2:
        mes_extenso = "fevereiro"
    elif mes == 3:
        mes_extenso = "março"
    elif mes == 4:
        mes_extenso = "abril"
    elif mes == 5:
        mes_extenso = "maio"
    elif mes == 6:
        mes_extenso = "junho"
    elif mes == 7:
        mes_extenso = "julho"
    elif mes == 8:
        mes_extenso = "agosto"
    elif mes == 9:
        mes_extenso = "setembro"
    elif mes == 10:
        mes_extenso = "outubro"
    elif mes == 11:
        mes_extenso = "novembro"
    else:
        mes_extenso = "dezembro"
    return f"{dia} de {mes_extenso} de {ano}."


print(data_extenso("04/11/2020"))
