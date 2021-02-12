"""
Escrevendo arquivos CSV

Montar uma lista ou dicionário que será passado para o método writer() que cria um objeto que permite a escrita.
Com o método writerow() fazemos a escrita linha a linha.

Método writer:

from csv import writer

with open("filmes.csv", "w") as arquivo:
    escritor_csv = writer(arquivo)
    filme = None
    escritor_csv.writerow(["Título", "Gênero", "Duração"])
    while filme != "sair":
        filme = input("Informe o nome do filme: ")
        if filme != "sair":
            genero = input(f"Informe o gênero de {filme}: ")
            duracao = input(f"Informe a duração de {filme}: ")
            escritor_csv.writerow([filme, genero, duracao])

# Método DicWriter

from csv import DictWriter

with open("filmes2.csv", "w") as arquivo:
    cabecalho = ["Título", "Gênero", "Duração"]
    escritor_csv = DictWriter(arquivo, fieldnames=cabecalho)
    escritor_csv.writeheader()
    filme = None
    while filme != "sair":
        filme = input("Informe o nome do filme: ")
        if filme != "sair":
            genero = input(f"Informe o gênero de {filme}: ")
            duracao = input(f"Informe a duração de {filme}: ")
            escritor_csv.writerow({"Título": filme, "Gênero": genero, "Duração": duracao})

"""

