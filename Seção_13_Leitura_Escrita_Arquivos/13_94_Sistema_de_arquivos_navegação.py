"""
Sistemas de arquivo e navegação

Alguns comandos

ls - lista os arquivos em  diretório
cd - muda de diretório
mkdir - cria um diretório
pwd - lista o caminho do diretório
cat - le o arquivo no terminal

Path

Absoluto: Da raiz até o arquivo

Relativo: ".." lista ou move um diretório acima na hierarquia, enquanto "." trabalha no diretório corrente

Para fazer uso da manipulação de arquivos do sistema operacional, precisamos importar o módulo os

import os

# listando o caminho absoluto do diretório corrente

print(os.getcwd())  # /Users/cadu/PycharmProjects/guppe/Seção_13_Leitura_Escrita_Arquivos

os.chdir("..")

print(os.getcwd())  # /Users/cadu/PycharmProjects/guppe

os.chdir("..")

print(os.getcwd())  # /Users/cadu/PycharmProjects

os.chdir("..")

print(os.getcwd())  # /Users/cadu

os.chdir("..")

print(os.getcwd())  # /Users

os.chdir("..")

print(os.getcwd())  # /

os.chdir("..")

print(os.getcwd())  # /

os.chdir("..")

print(os.getcwd())  # /

#  Checando se um diretório é absoluto ou relativo, retorna True ou Flase
print(os.path.isabs("/Users/cadu/PycharmProjects"))
#  Obs. Para casos Windows usar barras duplas para listar os diretórios "//Users//cadu//PycharmProjects"

#  Checando o sistema operacional
print(f"{os.name} \n{os.uname()}")

"""

import os

print(os.getcwd())

