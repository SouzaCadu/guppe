"""
gere uma matrix 4 x 4 com valores [1, 20] e transforme em
uma matriz triangular inferior, ou seja, atribuindo zero
a todos os valores acima da diagonal principal
"""

from random import randint

matriz1 = []

for i in range(4):
    aux = []
    for j in range(4):
        num = randint(1, 20)
        aux.append(num)
    matriz1.append(aux)

print(matriz1)

matriz2 = matriz1.copy()

for i in range(4):
    for j in range(4):
        if i < j:
            matriz2[i][j] = 0
            # print(f"{matriz2[i][j]}")

print(matriz2)