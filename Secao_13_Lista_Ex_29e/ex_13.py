"""
13) Faça um programa que permita que o usuário entre com diversos nomes e telefone para cadastro,
    e crie um arquivo com essas informações, uma por linha. O usuário finaliza a entrada com '0' para o telefone.
"""

import os
from valida_cadastro import valida_nome, valida_telefone

path = os.path.abspath(os.getcwd())

novo_arquivo = os.path.join(path, "lista_telefonica.csv")

print("Entre com diversos nomes e telefone para cadastro. Finalize a entrada com '0' para o telefone.")

try:
    while True:
        nome = str(input("Digite um nome: ")).strip().title()
        if valida_nome(nome) and len(nome) > 0:
            telefone = str(input("Digite um número de telefone: ")).strip()
            print()
            if valida_telefone(telefone):
                pass
            else:
                with open(novo_arquivo, "a", encoding="utf-8") as arquivo:
                    if telefone != '0':
                        informacoes = nome + ";" + telefone
                        arquivo.write(informacoes+"\n")
                    else:
                        break
                print("Telefone inválido!\n")
        else:
            print("\nNome inválido!\n")
    print("Informações inseridas no arquivo com sucesso!")
except FileNotFoundError:
    print("O arquivo informado não foi encontrado ou o programa não tem permissão para criar um diretório/pasta!")
except OSError:
    print("O SO não aceita caracteres especiais em nomes de arquivo!")