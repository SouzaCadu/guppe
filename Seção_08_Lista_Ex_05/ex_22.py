"""
crie uma função que receba como parâmetro um valor inteiro e gere
como saída pontos de exclamação
"""


def exclamacoes(num):
    lista = [n * '!' for n in range(1, num + 1)]
    for i in lista:
        print(i)


exclamacoes(10)