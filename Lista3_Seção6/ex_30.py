"""
Faça um programa para calcular as seguintes sequencias:
-> 1 + 2 + 3 + ... + n
-> 1 - 2 + 3 - ... + (2n - 1)
-> 1 + 3 + 5 + ... + (2n -1)
"""

print("Digite um valor n para calcular as sequencias:\n"
      "1 + 2 + 3 + ... + n \n"
      "1 - 2 + 3 - ... + (2n - 1) \n"
      "1 + 3 + 5 + ... + (2n - 1)")

n = int(input("Digite um valor: "))

seq1 = 0
seq2 = 0
seq3 = 0

for i in range(1, n+1):
    seq1 = seq1 + i

for j in range(1, 2 * n):
    if j % 2 != 0:
        seq2 = seq2 + j
    else:
        seq2 = seq2 - j

for k in range(1, 2 * n, 2):
    seq3 = seq3 + k

print(f"A soma da sequencia 1 é {seq1}\n"
      f"A soma da sequencia 2 é {seq2}\n"
      f"A soma da sequencia 3 é {seq3}")
