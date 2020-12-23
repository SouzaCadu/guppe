"""
leia uma matriz 5 x 5 e um valor X.
o programa deverá fazer uma busca desse valor na
matriz e ao final escrever a localização ou a mensagem
"não encontrado"
"""

from random import randint

matriz = []

for i in range(5):
    aux = []
    for j in range(5):
        num = randint(1, 100)
        aux.append(num)
    matriz.append(aux)

# print(matriz)

valor = int(input("Digite um valor entre 0 e 100 para verificar se ele está um uma matriz 5 x 5: "))

linha = -1
coluna = -1

for x in range(5):
    for y in range(5):
        if matriz[x][y] == valor:
            linha = x
            coluna = y

if linha == -1 and coluna == -1:
    print("Valor não localizado.")
else:
    print(f"{valor} está na linha {linha} coluna {coluna} da matriz.")
