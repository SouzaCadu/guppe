"""
escreva uma função que receba um número inteiro maior do que zero e retorne a soma
de todos os seus algarismos.
se o número for menor que zero o programa terminará com a mensagem "Número inválido"
"""


def soma_algorismos(n):
    """
    recebe um número verifica se é maior que 0, se menor finaliza o programa
    se maior soma os algarismos do número
    :param n: Qualquer número maior que zero
    :return: Retorna a soma dos algarismos de n
    """
    soma = 0
    if n > 0:
        var = str(int(n))
        for i in range(len(var)):
           soma += int(var[i])
        return f"A soma dos algarismos é {soma}"
    return f"Número inválido."


print(soma_algorismos(555.12))
print(soma_algorismos(125789))
print(soma_algorismos(-125789))
print(soma_algorismos(987452812.3215))
