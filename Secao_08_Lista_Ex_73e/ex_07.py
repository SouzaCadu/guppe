"""
faça uma função que receba uma temperatura em graus Celsius e converta em graus Fahrenheit
F = C * (9.0 / 5.0) + 32.0
"""

def conversor_celsius_fahrenheit(temp):
    """
    Conversor de temperatura de Celsius para Fahrenheit
    :param temp: Valor da temperatura em graus Celsius
    :return: Retorna o valor convertido em Fahrenheit
    """
    if temp < 0:
        return f"Insira um número positivo."
    f = temp * (9.0 / 5.0) * 32.0
    return f"{temp} graus Celsius equivale a {f:.2f} graus Fahrenheit."


print(conversor_celsius_fahrenheit(12.5))
print(conversor_celsius_fahrenheit(32.9))
print(conversor_celsius_fahrenheit(45.7))
