"""
Faça um programa que leia um inteiro positivo e imprima
todos os números naturais até N em ordem crescente
"""

print("Digite a quantidade de inteiros positivos que deseja obter a partir do zero:")
n = int(input("Digite a quantidade: "))

for i in range(0, n, 1):
    print(i, end=" ")
