"""
Lendo arquivos CSV (comma separated values)

Arquivos CSV podem ter diferentes separadores - ";" "," "|" " " "+" "=" - o importante que é que
os separadores sejam consistentes em todo o arquivo.

# forma não ideal de trabalhar com CSV em Python

with open("/Users/cadu/PycharmProjects/guppe/__Repositorio/lutadores.csv") as arquivo:
    dados = arquivo.read()
    dados = dados.split(",")[2:]
    print(dados)

# Método Reader
Permite qye iteremos sobre as linhas de um arquivo CSV como listas.

# Método DictReader
Permite que iteremos sobre as linhas de um arquivo CSV como um dicionário ordenado.

from csv import reader, DictReader

with open("/Users/cadu/PycharmProjects/guppe/__Repositorio/lutadores.csv") as arquivo:
    leitor_csv = reader(arquivo)
    next(leitor_csv)
    [print(f"\n{linha[0]} nasceu no(a)(s) {linha[1]} e mede {linha[2]}") for linha in leitor_csv]


with open("/Users/cadu/PycharmProjects/guppe/__Repositorio/lutadores.csv") as arquivo:
    leitor_csv = DictReader(arquivo)
    next(leitor_csv)
    [print(f"\n{linha['Nome']} nasceu no(a)(s) {linha['País']} e mede {linha['Altura (em cm)']}") for linha in leitor_csv]


"""


