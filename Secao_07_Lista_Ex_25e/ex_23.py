"""
faça um programa que leia uma matriz 3 x 3 (A)
e calcule
B = A ** 2
"""

from random import randint

matriz1 = [[(randint(1, 100)) for i in range(3)] for _ in range(3)]  # preenchendo a matriz
matriz2 = []

for i in range(3):
    aux = []
    for j in range(3):
        quadrado = matriz1[i][j] ** 2
        aux.append(quadrado)
    matriz2.append(aux)

print(f"A matriz {matriz1} ao quadrado é igual a {matriz2}.")
