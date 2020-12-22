"""
faça um programa que leia um vetor de 20 posições
e elimine os valores repetidos
"""

print("Insira 20 números, os valores repetidos serão eliminados ao final.")

v1 = []
count = 1

while count <= 20:
    valor = int(input(f"Digite {count} de 20 números: "))
    v1.append(valor)
    count += 1
    if count > 20:
        v1.sort()
        for i in v1:
            repete = v1.count(i)
            if repete > 1:
                del(v1[0:(repete - 1)])
        print(f"lista sem repetição {v1}.")
