"""
faça um programa que receba 6 números inteiros e mostre:
os números pares digitados
a soma dos números pares digitados
os números impares digitados
a quantidade de impares digitados
"""


print("Insira 6 números inteiros, pares ou impares.")

v = []
v1 = []
v2 = []
count = 1

while len(v) < 6:
    v.append(int(input(f"Digite {count} de 6 números: ")))
    count += 1

for i in v:
    if i % 2 == 0:
        v1.append(i)
    else:
        v2.append(i)
print(f"O vetor de valores pares é {v1} e soma {sum(v1)}\n"
      f"o vetor de valores impares é {v2} com {len(v2)} elementos.")
