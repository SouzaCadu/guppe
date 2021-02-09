"""
leia uma matriz 3 x 3 e calcule a soma da
diagonal secundária
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
n = 3

for i in range(3):  # percorre a lista do último item ao primeiro
    for j in range(3):  # percorre a lista do último item ao primeiro
        if i + j == n - 1:
            soma += matriz1[i][j]
            print(f"{soma, matriz1[i][j]}")

print(soma)