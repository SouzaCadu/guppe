"""
Receba um número inteiro e verifique se é par ou impar
"""

v1 = int(input("Insira um número inteiro para saber se é par ou ímpar:"))

if v1 % 2 == 0:
    print(f"{v1} é par.")
else:
    print(f"{v1} é ímpar.")
