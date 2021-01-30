"""
18) Faça um programa que leia um arquivo contendo o nome e o preço de diversos produtos (separados por linha),
    e calcule o total da compra.
"""

import os

print("Informe um arquivo contendo uma lista de compras com o nome e o preço de cada item separado por linha\n"
      "para saber o total da compra.\n")

path = input("Digite o caminho de um arquivo contendo uma lista de compras com o nome e o preço\n"
             "de cada item separado por linha: ")

try:
    with open(path, "r") as arquivo:
        lista = arquivo.read().strip().splitlines()
        valor_total = 0
        print(lista)
        for itens in range(len(lista)):
            item = lista[itens].split(":")
            preco = float(item[1])
            valor_total += preco
    print(f"O valor total da lista de compras é {valor_total:.2f}!")
except FileNotFoundError:
    print("\nArquivo não encontrado!")
except OSError:
    print("\nO SO não aceita caracteres especiais em nomes de arquivo!")
except ValueError:
    print("\nO modo que as informações se encontram no arquivo é inválido!")
