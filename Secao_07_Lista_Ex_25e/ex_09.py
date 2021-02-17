"""
leia uma matriz 3 x 3 e calcule a soma dos
elementos que estão abaixo da diagonal principal
"""

from random import randint

matriz1 = []

for i in range(3):
    aux = []
    for j in range(3):
        num = randint(1, 100)
        aux.append(num)
    matriz1.append(aux)

print(matriz1)

soma = 0

for i in range(3):
    for j in range(3):
        if i > j:
            soma += matriz1[i][j]
            print(f"{soma, matriz1[i][j]}")

print(soma)