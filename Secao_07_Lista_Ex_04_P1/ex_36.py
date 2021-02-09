"""
leia um vetor com 10 números reais, ordene os elementos e
imprima o vetor ordenado
"""

print("Insira 10 números reais.")

count = 1
vetor = []

while count <= 10:
    valor = float(input(f"Digite {count} de 10 números: "))
    vetor.append(valor)
    count += 1

vetor.sort()

print(f"Vetor ordenado {vetor}.")
