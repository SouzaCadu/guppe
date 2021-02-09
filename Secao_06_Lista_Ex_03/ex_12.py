"""
Faça um programa que leia um inteiro positivo e imprima todos
os números naturais de 0 até N em ordem decrescente
"""

print("Digite a quantidade números para a contagem regressiva.")
n = int(input("Digite o número: "))

for i in range(n, -1, -1):
    print(i, end=" ")
