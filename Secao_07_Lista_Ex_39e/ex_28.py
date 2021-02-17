"""
leia 10 números inteiros e armazene em um vetor.
crie 2 vetores e copie os impares para v1
e os pares para v2
ao final imprima os elementos utilizados em v1 e v2
"""

print("Insira 10 números inteiros, pares ou impares.")

v = []
v1 = []
v2 = []
count = 1

while len(v) < 10:
    v.append(int(input(f"Digite {count} de 10 números: ")))
    count += 1

for i in v:
    if i % 2 == 0:
        v1.append(i)
    else:
        v2.append(i)
print(f"O vetor de valores pares é {v1} com {len(v1)} elementos \n"
      f"o vetor de valores impares é {v2} com {len(v2)} elementos.")
