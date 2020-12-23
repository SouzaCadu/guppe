"""
faça um programa que preencha uma matriz 4 x 4
com produto do valor da linha e pelo número da coluna
"""

from random import randint

matriz = []

for i in range(4):
    aux = []
    for j in range(4):
        num = randint(1, 10)
        aux.append(num)
    matriz.append(aux)

print(matriz)

matriz1 = []

for x in range(4):
    aux1 = []
    for y in range(4):
        aux1.append(matriz[x][y] * y)
    matriz1.append(aux1)

print(matriz1)
