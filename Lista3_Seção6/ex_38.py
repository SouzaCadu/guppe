"""
faça um programa que calcule o termo pitagórico a, b, c
para o qual a + b + c = 1000
- termo pitagórico: a2 + b2 = c2
"""

valor = 1000

for a in range(valor + 1):
    for b in range(valor + 1):
        c = valor - a - b
        if ((a ** 2) + (b ** 2)) == (c ** 2):
            print(f"{a, b, c} satisfazem a condição do termo pitagórico.")
