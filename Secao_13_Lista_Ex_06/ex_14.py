"""
14) Dado um arquivo contendo um conjunto de nome e data nascimento (DD MM AAAA, isto é, 3 inteiros em sequência),
    faça um programa que leia o nome do arquivo e a data de hoje e construa outro arquivo contendo o nome e a
    idade de cada pessoa do primeiro arquivo.
"""

from datetime import date
import os

print("Informe um arquivo contendo um conjunto de nome e data nascimento. No mesmo diretório será construido\n"
      "outro arquivo contendo o nome e a idade de cada pessoa do primeiro arquivo.")

path = input("Digite o caminho de um arquivo contendo o nome e a data de nascimento: ")

# captura o nome do arquivo informado pelo usuário
basename = os.path.basename(path)

# extrai o nome do arquivo e a extensão
arquivo_aux, extensao = (os.path.splitext(basename))[0], (os.path.splitext(basename))[1]

novo_arquivo = os.path.join(os.path.dirname(path), arquivo_aux + "_idade" + extensao)

path2 = os.path.dirname(path)

nome_aux = arquivo_aux + "_idade" + extensao

try:
    with open(path, "r") as arquivo:
        arq_novo = open(novo_arquivo, "w", encoding='utf-8')
        base = arquivo.readlines()
        for linha in base:
            linha = linha.strip("\n").split()
            inicio = date(int(linha[4]), int(linha[3]), int(linha[2]))
            final = date.today()
            data_final = final - inicio
            idade = data_final.days // 365
            arq_novo.write(f'{linha[0]} tem {idade} anos')
            arq_novo.write('\n')
    arq_novo.close()
    print(f"\nIdade calculadas com sucesso em {path2}/{nome_aux} !")
except FileNotFoundError:
    print("\nO arquivo informado não foi encontrado ou o programa não tem permissão para criar um diretório/pasta!")
except OSError:
    print("\nO SO não aceita caracteres especiais em nomes de arquivo!")
except ValueError:
    print("\nO modo que as informações se encontram no arquivo é inválido!")
except IndexError:
    print("\nO modo que as informações se encontram no arquivo é inválido!")
