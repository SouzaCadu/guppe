"""
faça um programa que leia um número inteiro positivo N e
imprima todos os números pares de 0 até N em ordem crescente
"""

print("Digite a quantidade de números pares desejados de 0 até N.")
n = int(input("Quantidade de números pares desejados:"))

for i in range(0, n+1, 2):
    print(i, end=" ")
