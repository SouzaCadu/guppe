"""
leia dois vetores inteiros x e y, cada um com 5 elementos
assumindo que o usuário não informa elementos repetidos.
apresente:
soma entre x e y
produto entre x e y
diferença entre x e y
intersecção entre x e y
união entre x e y
"""

print("Insira 2 sequencias de 5 números reais.")

s1 = set({})
s2 = set({})
count = 1

for i in range(5):
    valor1 = float(input(f"Primeira sequencia, digite {count} de 5 números: "))
    s1.add(valor1)
    count += 1
print(f"Primeiro vetor {s1}.")

for i in range(5):
    valor2 = float(input(f"Segunda sequencia, digite {count} de 5 números: "))
    s2.add(valor2)
    count += 1
print(f"Segundo vetor {s2}.")

total_soma = 0
total_dif = 0
total_mult = 0

zip_object = zip(s1, s2)
for s1_i, s2_i in zip_object:
    soma = s1_i + s2_i
    total_soma += soma
    mult = s1_i * s2_i
    total_mult += mult
    dif = s1_i - s2_i
    total_dif += dif

print(f"A soma entre os conjuntos é {total_soma}.\n"
      f"O produto entre os conjuntos é {total_mult}.\n"
      f"A diferença entre os conjuntos é {total_dif}.\n"
      f"A intersecção entre os conjuntos é {s1.intersection(s2)}.\n"
      f"A união entre os conjuntos é {s1.union(s2)}.")
