"""
Receba 10 números e imprima o menor e o maior valor lido
"""

i = 1
menor = maior = 0

print("Digite 10 números e saiba qual é o maior e qual é o menor:")
while i <= 10:
    n = float(input("Digite um número:"))
    if n <= menor:
        menor = n
    if n >= maior:
        maior = n
    i = i + 1
print(f"O maior número é {maior} e o menor número é {menor}.")