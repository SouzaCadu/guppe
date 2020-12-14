"""
escreva um programa para calcular o valor da série para 5 termos
S = 0 + 1 / 2! + 2 / 4! + 3 / 6!...
"""

from math import factorial

print("Insira um valor para receber a soma S = 0 + 1 / 2! + 2 / 4! + 3 / 6!...")

n = int(input("Insira um número: "))

while n <= 0:
    n = int(input("Insira um número: "))

s = 0

for i in range(1, n + 1):
    s += i / (factorial(i * 2))
print(f"A soma da série é {s:.2f}.")
