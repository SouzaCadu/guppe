"""
faça um programa que leia um número inteiro positivo N e
imprima todos os números pares de 0 até N em ordem decrescente
"""

print("Digite a quantidade de números pares desejados de N até 0.")
n = int(input("Quantidade de números pares desejados: "))

for i in range(n, -1, -2):
    print(i, end=" ")
