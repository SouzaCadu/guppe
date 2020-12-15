"""
faça um programa que calcule o valor de S
S = 1/1 + 3/2 + 5/3 + 7/4 + ... + 99/50
"""

s = 0

for i in range(1, 51):
    s += ((2 * i) - 1) / i
print(f"O resultado é {s:.2f}.")