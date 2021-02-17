"""
faça uma função que receba um número N e retorne a soma dos algarismos em N!
"""


def soma_algarismos_fatorial(num):
    """
    Recebe um número N e retorne a soma dos algarismos em N!
    :param num: Qualquer número natural
    :return: soma dos algarismos
    """
    if num == 0 or num == 1:
        return 'O somatório é igual a 1'
    else:
        result = 1
        while num > 1:
            result = num * result
            num = num - 1
        result = str(result)
        soma = 0
        for i in result:
            n = int(i)
            soma += n
        return soma


print(soma_algarismos_fatorial(10))
