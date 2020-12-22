"""
faça um programa que leia dois vetores de 10 elementos.
crie um vetor que seja a união entre os 2 vetores anteriores
não deve conter números repetidos
"""

print("Insira 2 sequencias de 10 números reais.")

s1 = set({})
s2 = set({})
count = 1

for i in range(10):
    valor1 = float(input(f"Primeira sequencia, digite {count} de 10 números: "))
    s1.add(valor1)
    count += 1
print(f"Primeiro vetor {s1}.")

for i in range(10):
    valor2 = float(input(f"Segunda sequencia, digite {count} de 10 números: "))
    s2.add(valor2)
    count += 1
print(f"Segundo vetor {s2}.")

print(f"A união entre os conjuntos é {s1.union(s2)}.")
