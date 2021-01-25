"""
8) Faça um programa que leia o conteúdo de um arquivo e crie um arquivo
com o mesmo conteúdo, mas com todas as letras minúsculas convertidas para maiúsculas.
Os nomes dos arquivos serão fornecidos, via teclado, pelo usuário. A função
que converte maiúscula para minúscula é o toupper(). Ela é aplicada em cada caractere da string.
"""

import os

print("Informe o caminho completo de 2 arquivos. O primeiro deve ser um arquivo existente, o segundo será criado\n"
      "com o mesmo conteúdo do primeiro com todas as letras minúsculas substituídas por maiúsculas.")

path1 = str(input("Informe o caminho do primeiro arquivo: "))

while True:
    path2 = str(input("Informe o caminho do segundo arquivo: "))
    if os.path.isfile(path2):
        print("O arquivo já existe!")
    else:
        break

try:
    with open(path1, "r") as arquivo:
        with open(path2, "x") as novo_arquivo:
            texto = arquivo.readlines()
            for frase in texto:
                novo_arquivo.write(frase.upper())
    print(f"\nTexto alterado com sucesso em {path2}!")
except FileNotFoundError:
    print("\nArquivo informado não encontrado!")
