"""
2) Faça um programa que receba do usuário um arquivo texto e mostre na tela quantas linhas esse arquivo possui
"""

path = str(input("Informe o caminho do arquivo para saber quantas linhas o arquivo possui: "))

try:
    with open(path) as arquivo:
        linhas = arquivo.readlines()
        print(f"Em {path} há {len(linhas)} linhas.")
except FileNotFoundError:
    print("\nArquivo informado não encontrado!")
