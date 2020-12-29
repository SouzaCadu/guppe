"""
gerar uma matriz 10 x 10, onde os elementos são
A[i][j] = 2i + 7 - 2 se i < j
A[i][j] = 3i^2 - 1 se i = j
A[i][j] = 4i^2 + 5j^2 se i > j
"""

matriz = []

for i in range(10):
    aux = []
    for j in range(10):
        aux.append(0)
    matriz.append(aux)

for i in range(10):
    for j in range(10):
        if i < j:
            matriz[i][j] = ((2 * i) + 7 - 2)
        if i == j:
            matriz[i][j] = ((3 * i) ** 2) - 1
        if i > j:
            matriz[i][j] = ((4 * i) ** 2) - (5 * j) ** 2

print(matriz)


