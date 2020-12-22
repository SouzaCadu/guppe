"""
faça um programa que calcule o desvio padrão de um vetor v
contento 10 números, onde m é a média do vetor
"""

print("Insira 10 números para saber o desvio padrão.")

v1 = []
count = 1
soma = 0

while count <= 10:
    valor = int(input(f"Digite {count} de 10 números: "))
    v1.append(valor)
    count += 1
    if count > 10:
        print(f"A lista de números digitados é {v1}.")
        media = sum(v1) / len(v1)
        for i in v1:
            variancia = (i - media) ** 2
            soma += variancia

desv_pad = (1 / (len(v1) - 1) * soma) ** 0.5
print(f"O desvio padrão é {desv_pad:.2f}.")
