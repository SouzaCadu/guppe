"""
Faça um programa que receba 3 números e mostre-os em ordem crescente
"""

print("Digite 3 números e descubra qual a ordem crescente deles:")

n1 = float(input("Digite o primeiro número:"))
n2 = float(input("Digite o segundo número:"))
n3 = float(input("Digite o terceiro número:"))

lista = [n1, n2, n3]

lista.sort()

print(f"Ordem do números é {lista}.")
