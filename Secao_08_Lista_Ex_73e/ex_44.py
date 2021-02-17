"""
faça uma função que receba um vetor X de 30 elementos inteiros e
retorne, também por parâmetro, dois vetores A e B.
O vetor A e B deve ter os elementos pares e o vetor B
os elementos ímpares
"""


def vetor_par_impar(vetor):
    """
    Recebe um vetor X de 30 elementos inteiros e
    retorne dois vetores A e B.
    O vetor A deve ter os elementos pares e o
    vetor B os elementos ímpares
    :param lista: Qualquer vetor com 30 elementos inteiros
    :return: Dois vetores A com os valores pares e B com os valores impares
    """
    vetor_par = []
    vetor_impar = []
    if len(vetor) < 30:
        return "O vetor deve ter pelo menos 30 elementos."

    for i in vetor:
        if i != int(i):
            return "O vetor deve ter apenas números inteiros."

    for i in vetor:
        if i % 2 == 0:
            vetor_par.append(i)
        else:
            vetor_impar.append(i)
    return vetor_par, vetor_impar


lista = []
print('Informe 30 números inteiros para serem adicionados a um vetor:')
for i in range(30):
    number = int(input())
    lista.append(number)
print(vetor_par_impar(lista))
