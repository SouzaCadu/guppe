"""
9) Faça um programa que receba dois arquivos do usuário, e crie um terceiro arquivo com o conteúdo dos dois primeiros
   (o conteúdo do primeiro seguido do conteúdo do segundo).
"""

import os

print("Informe o caminho completo de 2 arquivos. Será criado um terceiro arquivo combinado o conteúdo dos dois\n"
      "arquivos anteriores.")

path1 = str(input("Informe o caminho do primeiro arquivo: "))
path2 = str(input("Informe o caminho do segundo arquivo: "))

while True:
    path3 = str(input("Informe o caminho do terceiro arquivo: "))
    if os.path.isfile(path3):
        print("O arquivo já existe!")
    else:
        break

try:
    with open(path1, "r") as arquivo1:
        with open(path2, "r") as arquivo2:
            with open(path3, "a") as novo_arquivo:
                novo_arquivo.write(arquivo1.read())
                novo_arquivo.write(arquivo2.read())
    print(f"\nTexto salvo com sucesso em {path3}!")
except FileNotFoundError:
    print("\nArquivo informado não encontrado!")