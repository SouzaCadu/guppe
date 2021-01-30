"""
16) Faça um programa que recebe um vetor de 10 números, converta cada um desses números para binário e grave a
    sequência de 0s e 1s em um arquivo texto. Cada número deve ser gravado em uma linha.
"""

import os

path = os.path.abspath(os.getcwd())

novo_arquivo = os.path.join(path, "numeros_binarios.txt")

print(f"Insira 10 números inteiros que serão convertidos em números binários e salvos em {novo_arquivo}.")

v1 = []
count = 1

while count <= 10:
    valor = int(input(f"Digite {count} de 10 números: "))
    v1.append(valor)
    count += 1
    if count > 10:
        with open(novo_arquivo, "w") as arquivo:
            for i in v1:
                arquivo.write("{0}\n".format(bin(i)))
            print(f"Informações inseridas no arquivo com sucesso em {novo_arquivo}!")
