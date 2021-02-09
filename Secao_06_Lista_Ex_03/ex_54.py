"""
faça um programa que receba um número inteiro maior que 1,
e verifique se o número fornecido é primo ou não
"""

n = int(input("Digite um número para verificar se ele é primo: "))

if n <= 0:
    print("Valor inválido.")
    n = int(input("Digite um número para verificar se ele é primo: "))

mult = 0

for i in range(2, n):
    if n % i == 0:
        mult += 1
if mult == 0:
    print(f"{n} é um primo.")
else:
    print(f"{n} não é um número primo.")