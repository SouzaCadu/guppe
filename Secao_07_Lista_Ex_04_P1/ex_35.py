"""
faça um programa que leia dois números a e b (positivos e menores que 10000)
- crie um vetor onde cada posição é um algarismo do número.
a primeira posição deve ser o número menos significativo
- crie um vetor que seja a soma de a e b, usando os valores
construidos anteriormente
"""

print("Insira dois valores, positivos e menores que 10000.")

a = int(input("Digite o primeiro valor: "))
if a < 0 or a > 10000:
    a = int(input("Digite o primeiro valor: "))

b = int(input("Digite o segundo valor: "))
if b < 0 or b > 10000:
    b = int(input("Digite o segundo valor: "))

a = str(a)
b = str(b)

vetor_a = []
vetor_b = []

for i in a:
    vetor_a.append(int(i))
vetor_a.sort()

for i in b:
    vetor_b.append(int(i))
vetor_b.sort()

print(f"A soma de {vetor_a} + {vetor_b} é {sum(vetor_a) + sum(vetor_b)}.")
