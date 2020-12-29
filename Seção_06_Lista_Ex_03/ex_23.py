"""
Faça um algorítimo que leia um número positivo e imprima
seus divisores
"""

print("Informe um número inteiro para saber seus divisores.")

n = int(input("Digite um número inteiro:"))

for i in range(1, n + 1):
    if n % i == 0:
        print(i, end=" ")
