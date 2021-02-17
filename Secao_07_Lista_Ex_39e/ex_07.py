"""
faça um programa leia 10 números inteiros e os armazene em um vetor
Imprima o vetor, o maior elemento e a posição que ele se encontra
"""

print("Insira 10 números para saber o maior e a posição que ele se encontra.")

v1 = []
count = 1

while count <= 10:
    valor = int(input(f"Digite {count} de 10 números: "))
    v1.append(valor)
    count += 1
    if count > 10:
        for i, j in enumerate(v1):
            if j == max(v1):
                indice = i
        print(f"O maior valor é {max(v1)} e a posição é {indice}.")

