"""
Faça um programa que calcule e mostre a soma dos 50
primeiros números pares
"""

n = 0

for i in range(2, 101, 2):
    print(i, end=' ')
    n = n + i
print()
print(n)
