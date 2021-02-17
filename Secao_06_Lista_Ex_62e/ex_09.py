"""
Faça um programa que leia um número inteiro N e depois
imprima os N primeiros números naturais impares
"""

print("Digite a quantidade de números impares inteiros desejada:")
n = int(input("Digite a quantidade desejada: "))

for i in range(1, n + n, 2):
    print(i, end=" ")
