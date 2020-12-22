"""
ler 2 conjuntos de 5 números reais, armazenando-os em vetores
calcular o produto escalar entre eles, dado por (x1 * y1) + (x2 * y2) + ... +(xn + yn)
"""

print("Insira 2 sequencias de 5 números reais para descobrir o produto escalar deles.")

v1 = []
v2 = []
v3 = []
count = 1

for i in range(5):
    valor1 = float(input(f"Primeira sequencia, digite {count} de 5 números: "))
    v1.append(valor1)
    count += 1

print(f"Primeiro vetor {v1}.")

count = 1
for i in range(5):
    valor2 = float(input(f"Segunda sequencia, digite {count} de 5 números: "))
    v2.append(valor2)
    count += 1

print(f"Segundo vetor {v2}.")

zip_object = zip(v1, v2)
for v1_i, v2_i in zip_object:
    v3.append(v1_i * v2_i)

print(f"Resultado {sum(v3)}.")
