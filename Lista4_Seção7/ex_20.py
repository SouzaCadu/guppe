"""
escreva um programa que leia números inteiros entre [0, 50] e os
armazene em vetor com 10 posições.
preencha um segundo vetor apenas com números ímpares do
primeiro vetor.
imprima os 2 vetores com 2 elementos por linha
"""

print("Insira 10 números reais entre 0 e 50.")

v1 = []
v2 = []
count = 1

while count <= 10:
    valor = float(input(f"Digite {count} de 10 números: "))
    if valor in range(51):
        v1.append(valor)
        count += 1
    else:
        valor = float(input(f"Digite {count} de 10 números: "))
    if count > 10:
        for i in v1:
            if i % 2 != 0:
                v2.append(i)
        for i, j in enumerate(range(0, len(v1) - 1)):
            print(f"Vetor original {v1[i], v1[i + 1]}.")
        for i, j in enumerate(range(0, len(v2) - 1)):
            print(f"Vetor com números ímpares {v2[i], v2[i + 1]}.")
