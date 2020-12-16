"""
faça um programa que some os termos de valor par da
sequencia de Fibonacci, cujos valores sejam menores
que 4 milhões
"""

from math import sqrt

soma = 0

for n in range(100):
    fibonacci = int(((1 + sqrt(5)) ** n - (1 - sqrt(5)) ** n) / (2 ** n * sqrt(5)))
    if fibonacci <= 4000000:
        if fibonacci % 2 == 0:
            soma = soma + fibonacci
            print(f"{fibonacci}", end=" ")

print(f"A soma é {soma}.")

