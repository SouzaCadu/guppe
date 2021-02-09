"""
faça um programa para ler 10 números diferentes armazenados em um vetor,
o usuário deve ser alertado se fornecer um número repetido.
exibir na tela o vetor final
"""

print("Insira 10 números inteiros diferentes.")

v = []
count = 1

while len(v) < 10:
    valor = int(input(f"Digite {count} de 10 números: "))
    if valor in v:
        print("Valor repetido. Insira um valor diferente.")
    else:
       v.append(valor)
       count += 1

print(f"O vetor final é {v}.")
