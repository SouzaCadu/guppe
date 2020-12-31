"""
escreva uma função que gera um triangulo de altura e lados n
e base 2 * n - 1
"""


def triangulo(num):
    for i in range(1, num + 1):
        tri = (' ' * (num - i)) + ('*' * (2 * i - 1))
        print(tri)


triangulo(6)
triangulo(10)