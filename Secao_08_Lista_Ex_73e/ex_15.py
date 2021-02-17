"""
crie um programa que receba 3 valores obrigatoriamente maiores que zero
representando as medidas dos 3 lados de um triângulo:
- determine se todos os lados formam um triângulo
- determine qual o tipo de triângulo
"""

def avalia_triangulo(l1, l2, l3):
    """
    Recebe 3 valores obrigatoriamente maiores que zero,
    determina se é possível formar um triângulo e de qual
    tipo
    :param l1: Lado do triângulo
    :param l2: Lado do triângulo
    :param l3: Lado do triângulo
    :return: Se é possível formar um triângulo e de
             qual tipo
    """
    if l1 <= 0 or l2 <= 0 or l3 <= 0:
        return "Com esses valores não é possível formar um triângulo."
    elif l1 < l2 + l3 and l2 < l1 + l3 and l3 < l1 + l2:
        if l1 == l2 == l3:
            return "Os valores informados formam um triângulo equilátero."
        elif l1 != l2 != l3:
            return "Os valores informados formam um triângulo escaleno."
        return "Os valores informados formam um triângulo isóceles."
    return "Com esses valores não é possível formar um triângulo."


print(avalia_triangulo(12, 12, 12))
print(avalia_triangulo(3, 4, 5))
print(avalia_triangulo(15, 15, 22))
print(avalia_triangulo(17, 32, 122))
print(avalia_triangulo(-12, 12, 12))