"""
faça um programa que receba do usuário dois vetores A e B
com 10 números inteiros cada.
crie um novo vetor C sendo A - B
"""


print("Insira 2 sequencias de 10 números reais.")

v1 = []
v2 = []
count = 1
diferenca = []

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

zip_object = zip(v1, v2)
for v1_i, v2_i in zip_object:
    diferenca.append(v1_i - v2_i)

print(f"Diferença entre o primeiro e o segundo {diferenca}.")
