"""
faça um programa que calcule o maior número palíndromo
feito a partir de 2 números de 3 digitos
"""

maior = 0

for i in range(100, 1000):
    for j in range(100, 1000):
        x = i * j
        if str(x) == str(x)[::-1]:
            if x > maior:
                maior = x
print(f"O maior palíndromo gerado a partir do produto de dois números de três digitos é {maior}")