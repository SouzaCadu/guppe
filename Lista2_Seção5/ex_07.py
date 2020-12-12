"""
Receba dois números:
- mostre o maior
- se os dois forem iguais, imprima 'Números iguais'
"""

print("Compare 2 números.")

v1, v2 = float(input("Digite o primeiro número:")), float(input("Digite o segundo número:"))

if v1 > v2:
    print(f"O maior número é {v1}.")
elif v2 > v1:
    print(f"O maior número é {v2}.")
else:
    print("Números iguais.")
