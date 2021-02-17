"""
faça um programa que permita ao usuário entrar com
uma matriz 3 x 3 de números inteiros.
em seguida gere um array unidimensional pela soma
dos números de cada coluna da matriz e mostrar esse array
"""

print("Insira 9 valores para compor uma matriz 3 x 3\n"
      "e receber a soma dos valores das colunas.")

matriz = []
soma = [0, 0, 0]
count = 1

while count <= 9:
    for i in range(3):
        aux = []
        for j in range(3):
            valor = int(input(f"Digite {count} de 9 números: "))
            aux.append(valor)
            count += 1
        matriz.append(aux)
    if count > 9:
        print(f"A matriz de números digitados é {matriz}.")

for x in range(3):
    for y in range(3):
        soma[y] = soma[y] + matriz[x][y]
        # print(soma[y], matriz[x][y])
print(f"A soma da matriz informada é {soma}.")
