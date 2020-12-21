"""
faça um programa que leia um vetor de 10 posições e verifique se
existem valores iguais e os escreva na tela
"""

print("Insira 10 números para saber se existem valores iguais.")

v1 = []
count = 1

while count <= 10:
    valor = int(input(f"Digite {count} de 10 números: "))
    v1.append(valor)
    count += 1
    if count > 10:
        v1.sort()
        for i in v1:
            repete = v1.count(i)
            if repete > 1:
                print(f"O {i} repete {repete} vezes.")
