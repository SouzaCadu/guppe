"""
escreva um programa que leia um número inteiro positivo N e em seguida imprima N
linhas do chamado Triangulo de Floyd.
"""

n = int(input("Digite o valor para o Triângulo de Floyd: "))

linhas = 1

for i in range(1, n + 1):
    for j in range(1, i + 1):
        print(linhas, end=" ")
        linhas = linhas + 1
    print()
