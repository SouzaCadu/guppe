"""
leia uma matriz 3 x 3 e calcule e imprima a
matriz transposta
"""

from random import randint

matriz = []

for i in range(3):
    aux = []
    for j in range(3):
        num = randint(1, 100)
        aux.append(num)
    matriz.append(aux)

print(matriz)

n = len(matriz)
transpose = [[row[i] for row in matriz] for i in range(n)]
print (transpose)
