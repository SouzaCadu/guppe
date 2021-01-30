"""
23) Escreva um programa que leia a profissão e o tempo de serviço (em anos) de cada um dos 5 funcionários de uma empresa
    e armazene-os no arquivo "emp.txt". Cada linha do arquivo corresponde aos dados de um funcionário.
"""

import os

path = os.path.abspath(os.getcwd())

novo_arquivo = os.path.join(path, "emp.txt")

print(f"Insira os dados de profissão e o tempo de serviço (em anos) de cada um dos 5 funcionários da empresa\n"
      f"as informações ficaram salvas em {novo_arquivo}.")

lista = []
count = 1

while count <= 5:
    profissao = input(f"Digite a profissao do {count} funcionário: ")
    temp_serv = input(f"Digite o tempo de serviço do {count} funcionário: ")
    lista.append((profissao, temp_serv))
    count += 1
    if count > 5:
        with open(novo_arquivo, "w") as arquivo:
            for item in lista:
                arquivo.write(f"{item}\n")
            print(f"Informações inseridas no arquivo com sucesso em {novo_arquivo}!")

with open(novo_arquivo) as res:
    print(res.read())
