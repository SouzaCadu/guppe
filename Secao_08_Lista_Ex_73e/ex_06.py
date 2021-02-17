"""
faça uma função que receba 3 números inteiros como parâmetro,
representando horas, minutos e segundos, e os converta em segundos
"""


def conversor_segundos(horas, minutos, segundos):
    """
    Recebe 3 argumentos, horas, minutos e segundos e transforma em segundos
    :param horas: número de horas
    :param minutos: número de minutos
    :param segundos: número de segundos
    :return: retorna o quantidade de segundos correspondente as horas, minutos e segundos informados
    """
    soma = 0
    soma += int(horas) * 3600
    soma += int(minutos) * 60
    soma += int(segundos)
    return f"A conversão de {horas}:{minutos}:{segundos} em segundos é {soma}."


print(conversor_segundos(12, 36, 48))
print(conversor_segundos(18, 10, 5))
