"""
peça ao usuário para digitar 10 valores, e ordene de maneira
crescente assim que ele for digitado
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

print(f"Vetor final ordenado {vetor}.")
