"""
7) Faça um programa que receba do usuário um arquivo texto. Crie outro arquivo texto contendo o texto do arquivo
   de entrada, mas com as vogais substituídas por '*'
"""

import os

print("Informe o caminho completo de um arquivo. Um novo arquivo do mesmo tipo será criado no mesmo diretório,\n"
      "substituindo as vogais por '*'.")

path = str(input("Informe o caminho do arquivo: "))

# captura o nome do arquivo informado pelo usuário
basename = os.path.basename(path)

# extrai o nome do arquivo e a extensão
arquivo_aux, extensao = (os.path.splitext(basename))[0], (os.path.splitext(basename))[1]

novo_arquivo = os.path.join(os.path.dirname(path), arquivo_aux + "vogais_*" + extensao)

path2 = os.path.dirname(path)

nome_aux = arquivo_aux + "vogais_*" + extensao

try:
    with open(path, "r") as arquivo:
        with open(novo_arquivo, "w") as novo_arquivo:
            novo_arquivo.write("".join(map(lambda x: '*' if x in "aeiouAEIOU" else x, arquivo.read())))
    print(f"\nTexto alterado com sucesso em {path2}/{ nome_aux} !")
except FileNotFoundError:
    print("\nArquivo informado não encontrado!")

