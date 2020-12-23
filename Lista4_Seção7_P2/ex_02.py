"""
declare uma matriz 5 x 5. preencha a diagonal
principal com 1 e com zero os demais elementos
"""

matriz = [[], [], [], [], []]

count = 0

while count <= 16:
    for i in range(0, 5):
        matriz[i].insert(1, 0)
        count += 1


for j in range(0, 5):
    matriz[j].insert(j, 1)

print(matriz)

