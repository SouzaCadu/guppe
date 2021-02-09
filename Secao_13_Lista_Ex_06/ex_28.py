"""
28) Faça um programa que receba como entrada o nome de um arquivo de entrada e o nome de um arquivo de saída.
    Cada linha do arquivo de entrada possui colunas de tamanho de 30 caracteres. No arquivo de saída deverá ser
    escrito o arquivo de entrada de forma inversa. Veja um exemplo:

    Arquivo de entrada:
    Hoje é dia de prova de AP
    A prova está muito fácil
    vou tirar uma boa nota

    Arquivo de saída:
    Aton aob amu ratir uov
    Licáf otium átse avorp A
    PA ed avortp ed aid é ejoH
"""


import os

print("Informe o caminho completo de 2 arquivos. O conteúdo inserido no  primeiro arquivo será limitado"
      "em 30 caracteres por linha. O segundo será criado com o mesmo conteúdo do primeiro em ordem inversa.")

path1 = str(input("Informe o caminho do primeiro arquivo: "))

while True:
    path2 = str(input("Informe o caminho do segundo arquivo: "))
    if os.path.isfile(path2):
        print("O arquivo já existe!")
    else:
        break

try:
    with open(path1, "w") as arquivo:
        texto = str(input("\nInsira o texto do arquivo de entrada: ")).strip()
        conteudo = ""
        for palavra in range(len(texto)):
            conteudo += f"{texto[palavra]}\n" if (palavra + 1) % 30 == 0 else f"{texto[palavra]}"
        arquivo.write(conteudo)
    with open(path1, "r") as leitura:
        with open(path2, "w") as novo_arquivo:
            novo_arquivo.write(leitura.read()[::-1])
    print(f"\nTexto alterado com sucesso em {path2}!")
except FileNotFoundError:
    print("\nArquivo informado não encontrado!")
