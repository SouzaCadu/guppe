"""
leia duas matrizes 4 x 4 e escreva uma terceira
com os maiores valores em cada posição
das matrizes anteriores
"""

from random import randint

matriz1 = []
matriz2 = []
matriz3 = []

for i in range(4):
    aux = []
    for j in range(4):
        num = randint(1, 100)
        aux.append(num)
    matriz1.append(aux)

for x in range(4):
    aux = []
    for y in range(4):
        num = randint(1, 100)
        aux.append(num)
    matriz2.append(aux)

for z in range(4):
    aux = []
    for w in range(4):
        if matriz1[z][w] > matriz2[z][w]:
            aux.append(matriz1[z][w])
        else:
            aux.append(matriz2[z][w])
    matriz3.append(aux)

print(f"{matriz1}\n"
      f"{matriz2}\n"
      f"{matriz3}\n")
