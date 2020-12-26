"""
faça um programa que leia duas matrizes 3 x 3 (A e B)
e calcule
C = A * B
"""

from random import randint

matriz1 = [[(randint(20, 30)) for i in range(3)] for _ in range(3)]  # preenchendo a matriz
matriz2 = [[(randint(10, 20)) for i in range(3)] for _ in range(3)]  # preenchendo a matriz
matriz3 = []

for i in range(3):
    aux = []
    for j in range(3):
        mult = matriz1[i][j] * matriz2[i][j]
        aux.append(mult)
    matriz3.append(aux)

print(f"O produto das matrizes {matriz1} pela {matriz2} é {matriz3}.")
