"""
leia uma matriz 4 x 4, conte e escreva
quantos valores maiores que 10 ela possui
"""

from random import randint

matriz = [[], [], [], []]

count = 0

while count <= 15:
    for i in range(0, 4):
        matriz[i].insert(1, randint(1, 100))
        count += 1

print(matriz)

maior_10 = 0

for i in range(0, 4):
    for j in range(0, 4):
        if matriz[i][j] >= 10:
            maior_10 += 1

print(f"Total de elementos acima de 10 é {maior_10}.")