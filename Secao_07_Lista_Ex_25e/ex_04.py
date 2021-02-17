"""
leia uma matriz 4 x 4, imprima a matriz e retorne
a localização linha e coluna do maior valor
"""

from random import randint

matriz = []
maior = 0

for i in range(4):
    aux = []
    for j in range(4):
        num = randint(1, 100)
        aux.append(num)
    matriz.append(aux)
print(matriz)

for x in range(4):
    for y in range(4):
        if matriz[x][y] >= maior:
            maior = matriz[x][y]
            linha = x
            coluna = y

print(f"O maior elemento é o {maior} e está na linha {linha} coluna {coluna}.")
