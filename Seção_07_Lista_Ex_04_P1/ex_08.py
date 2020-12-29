"""
crie um programa que lê 6 valores inteiros e, em seguida, mostre
na tela os valores lidos na ordem inversa
"""

print("Insira 6 números inteiros, que serão exibidos em ordem inversa.")

v1 = []
count = 1

while count <= 6:
    valor = int(input(f"Digite {count} de 6 números: "))
    v1.append(valor)
    count += 1
    if count > 6:
        v1.reverse()
        print(f"{v1}.")
