"""
Faça um programa que leia 10 inteiros e imprima a média
"""

i = 1
soma = 0
print("Digite 10 valores inteiros para saber a média aritmética:")
while i <= 10:
    n = int(input("Digite um valor: "))
    soma = soma + n
    i = i + 1
print(f"A média aritmética dos números digitados é {soma/10:.2f}.")