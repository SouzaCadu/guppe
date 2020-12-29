"""
faça um programa que leia dois vetores de 10 posições e calcule outro vetor
contendo nas posições pares os valores do primeiro vetor e nas posições
impares os valores do outro vetor
"""

print("Insira 2 sequencias de 10 números reais.")

v1 = []
v2 = []
v3 = []
ind1 = 0
ind2 = 0
count = 1

for i in range(10):
    valor1 = float(input(f"Primeira sequencia, digite {count} de 10 números: "))
    v1.append(valor1)
    count += 1

print(f"Primeiro vetor {v1}.")

for i in range(10):
    valor2 = float(input(f"Segunda sequencia, digite {count} de 10 números: "))
    v2.append(valor2)
    count += 1

print(f"Segundo vetor {v2}.")

for i, j in enumerate(range(20)):
    if i % 2 == 0:
        v3.append(v1[ind1])
        ind1 += 1
    else:
        v3.append(v2[ind2])
        ind2 += 1

print(f"Terceiro vetor {v3}.")
