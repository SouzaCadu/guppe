"""
faça um programa para gerar automaticamente números entre
0 e 99 em uma matriz 5 x 5, sem repetições, imprima a matriz
"""

from random import randint, choice

conjunto = set({})
matriz = []

while len(conjunto) < 25:
    num = randint(0, 99)
    conjunto.add(num)
lista = list(conjunto)
print(lista, len(lista))

for i in range(5):
    aux = []
    for j in range(5):
        num = choice(lista)
        aux.append(num)
        lista.remove(num)
    matriz.append(aux)

print(matriz)
