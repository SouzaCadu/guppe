"""
faça um programa que leia um vetor de 15 posições
e elimine as posições de valor 0, movendo todos
elementos a frente do zero uma posição atrás no vetor
"""

print("Insira 15 números inteiros, valores iguais 0 serão removidos ao final.")

v = []
count = 1

while len(v) < 15:
    v.append(int(input(f"Digite {count} de 15 números: ")))
    count += 1

vetor = [i for i in v if i > 0]

print(f"O vetor final é {vetor}.")
