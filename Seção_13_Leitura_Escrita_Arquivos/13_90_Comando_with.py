"""
Bloco with

para trabalhar com arquivos seguimos os seguintes passos:
1 - abrir o arquivo
2 - manipular o arquivo
3 - fechar o arquivo

O bloco with cria um contexto de trabalho onde os recursos são finalizados depois que o bloco é executado. No caso
dos arquivos ele abre e fecha o arquivo dentro do contexto, sendo a forma recomendada de trabalho com arquivos em
Python.


with open("texto.txt") as arquivo:
    print(arquivo.readline())

"""
