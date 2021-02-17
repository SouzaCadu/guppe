"""
leia um vetor de 10 posições e atribua 0 para todos os
elementos qye possuírem valores negativos
"""

print("Insira 10 números reais, se negativos serão substituidos por zero.")

v1 = []
count = 1

while count <= 10:
    valor = float(input(f"Digite {count} de 10 números: "))
    v1.append(valor)
    count += 1
    if count > 10:
        for i, j in enumerate(v1):
            if j < 0:
                v1[i] = 0
        print(f"Vetor é {v1}.")
