"""
faça um programa que leia uma matriz 3 x 6 com valores reais
- imprima a soma de todos os elementos das colunas impares
- imprima a média aritmética dos colunas 2 e 4
- substitua os valores da sexta coluna pela soma
  dos valores das colunas 1 e 2
- imprima a matriz modificada
"""

from random import randint

matriz = []

for i in range(3):
    aux = []
    for j in range(6):
        num = randint(1, 100)
        aux.append(num)
    matriz.append(aux)

print(matriz)

soma_colunas_imp = 0

for x in range(3):
    for y in range(0, 5, 2):
        soma_colunas_imp += matriz[x][y]
print(f"A soma das colunas ímpares é {soma_colunas_imp}.")

media_colunas_2_4 = 0

for k in range(3):
    media_colunas_2_4 += (matriz[k][1] + matriz[k][3]) / 2
print(f"A média da segunda e quarta colunas é {media_colunas_2_4}")

for l in range(3):
    matriz[l][5] = matriz[l][0] + matriz[l][1]
print(f"A matriz modificada é {matriz}.")
