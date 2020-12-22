"""
considere um vetor A com 11 elementos
A1 < A2 < ... < A6 > A7 A8> ... > A11, ou seja,
em ordem crescente até o sexto elemento e em
ordem decrescente a partir do sétimo.
"""

print("Insira 11 valores reais")

vetor = []
v1 = []
v2 = []
count = 1

while count <= 11:
    valor = float(input(f"Digite {count} de 11 números: "))
    vetor.append(valor)
    count += 1

v1 = vetor[:6]
v1.sort()
print(v1)
v2 = vetor[6:]
v2.reverse()
print(v2)

print(f"Vetor ordenado {v1 + v2}.")
