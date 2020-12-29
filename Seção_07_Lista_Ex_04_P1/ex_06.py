"""
faça um programa que receba do usuário um vetor com 10 posições
em seguida imprima o maior e o menor valor
"""

print("Insira 10 números para saber o maior e o menor")

v1 = []
count = 1

while count <= 10:
    valor = float(input(f"Digite {count} de 10 números: "))
    v1.append(valor)
    count += 1
    if count > 10:
        print(f"O maior valor é {max(v1)} e o menor valor é {min(v1)}.")

