"""
faça uma função que receba a distância em KM e a quantidade de litros
de gasolina consumidos por um carro e calcule o consumo em
KM / L e escreva a mensagem de acordo com a tabela
- se menor que 8: venda o carro
- entre 8 e 14 econômico
- maior que 14 super econômico
"""


def avalia_consumo(km, litros):
    """
    Calcule o consumo em KM / L e escreva a mensagem de acordo com a tabela
    - se menor que 8: venda o carro
    - entre 8 e 14 econômico
    - maior que 14 super econômico
    :param km: Distância percorrida em km
    :param litros: Quantidade de gasolina utilizada em litros
    :return: Consumo no trajeto percorrido
    """
    consumo = km / litros
    if consumo < 8:
        return "Venda o carro!"
    elif 8 <= consumo <= 14:
        return "Econômico!"
    return f"Super econômico!"


print(avalia_consumo(125, 10))
print(avalia_consumo(250, 32))
print(avalia_consumo(375, 11))
