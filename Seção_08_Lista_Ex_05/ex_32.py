"""
faça uma função chamada "simplificada" que recebe como parâmetro o numerador
e o denominador de uma fração. Essa função deve simplificar a fração recebida
dividindo o numerador e o denominador pelo maior fator possível
"""


def simplificada(numerador, denominador):
    """
    Calcula o máximo divisor comum entre dois números inteiros positivos
    :param numerador: Qualquer número positivo
    :param denominador: Qualquer número positivo
    :return: Máximo divisor comum dos números informados
    """
    if numerador <= 0 or denominador <= 0:
        print("Valores inválidos! Informe valores maiores que zero!")
    mdc = numerador
    while numerador % mdc != 0 or denominador % mdc != 0:
        mdc = mdc - 1
    return mdc


print(simplificada(36, 60))
