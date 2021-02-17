"""
15) Faça um programa que receba como entrada o ano corrente e o nome de dois arquivos: um de entrada e outro de saída.
    Cada linha do arquivo de entrada contém o nome de uma pessoa (ocupando 40 caracteres) e o seu ano de nascimento.
    O programa deverá ler o arquivo de entrada e gerar um arquivo de saída onde aparece
    o nome da pessoa seguida por uma string que representa a sua idade.
    . Se a idade for menor do que 18 anos, escreva "menor de idade"
    . Se a idade for maior do que 18 anos, escreva "maior de idade
    . Se a idade for igual a 18 anos, escreva "entrando na maior idade"
"""


from datetime import date
import os

print("Informe o ano corrente, um arquivo contendo um conjunto de nome e data nascimento e um arquivo onde será\n"
      "gravado o nome da pessoa, idade e\n"
      "se a idade for menor do que 18 anos 'menor de idade'\n"
      "se a idade for maior do que 18 anos 'maior de idade'\n"
      "se a idade for igual a 18 anos 'entrando na maior idade'")

ano_corrente = int(input("Digite o ano corrente: "))

path1 = input("Digite o caminho de um arquivo contendo o nome e a data de nascimento: ")

path2 = input("Digite o caminho onde o arquivo de saída será salvo: ")

try:
    with open(path1, "r") as arquivo:
        arq_novo = open(path2, "w", encoding='utf-8')
        base = arquivo.readlines()
        for linha in base:
            linha = linha.strip("\n").split()
            idade = ano_corrente - int(linha[4])
            if idade < 18:
                fx_idade = 'menor de idade'
            elif idade > 18:
                fx_idade = 'maior de idade'
            else:
                fx_idade = 'entrando na maior idade'
            arq_novo.write(f'{linha[0]} tem {idade} anos, {fx_idade}')
            arq_novo.write('\n')
    arq_novo.close()
    print(f"\nIdade calculadas com sucesso em {path2}!")
except FileNotFoundError:
    print("\nO arquivo informado não foi encontrado ou o programa não tem permissão para criar um diretório/pasta!")
except OSError:
    print("\nO SO não aceita caracteres especiais em nomes de arquivo!")
except ValueError:
    print("\nO modo que as informações se encontram no arquivo é inválido!")
except IndexError:
    print("\nO modo que as informações se encontram no arquivo é inválido!")
