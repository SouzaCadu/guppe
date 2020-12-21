"""
faça um vetor de tamanho 50 preenchido com o valor
(i + 5 * i) % (i + 1) sendo i a posição elemento no vetor
"""

v1 = []

for i, j in enumerate(range(51)):
    v1.append((i + 5 * i) % (i + 1))
print(v1)