"""
escreva uma função que gere um triângulo lateral de
altura 2*n-1 e n de largura
"""


def triangulo_lateral(num):
    linha = ""
    for i in range (2 * num - 1):
        if i < num:
            linha += "*" * (i + 1) + "\n"
        else:
            linha += (2 * num - (i + 1)) * "*" + "\n"
    return linha

print(triangulo_lateral(12))