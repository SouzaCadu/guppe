"""
12) Abra um arquivo texto, calcule e escreva o número de caracteres, o número de linhas e o número de palavras neste
    arquivo. Escreva também quantas vezes cada letra ocorre no arquivo (ignorando letras com acento).
    Obs.: palavras são separadas por um ou mais caracteres espaços, tabulação ou nova linha.
"""

from collections import Counter

print("Digite o caminho do arquivo para saber quantas vezes cada letra do alfabete aparece no arquivo selecionado.")
path = str(input("Informe o caminho do arquivo: "))

try:
    with open(path, "r") as arquivo:
        texto = arquivo.readlines()
        linhas = len(texto)
        palavras = [Counter(str(texto).split())]
        total_palavras = {k: sum(d[k] for d in palavras) for k in palavras[0]}
        dicts = []
        for frase in texto:
            dicts.append(Counter(frase))
        total_caracteres = {k: sum(d[k] for d in dicts) for k in dicts[0]}
    with open(path, "a") as arquivo:
        arquivo.write(f"\ntotal de linhas: {linhas}\n")
        arquivo.write(f"\ntotal de palavras: {total_palavras}\n")
        arquivo.write(f"\ntotal de caracteres: {total_caracteres}\n")
        print(f"Dados inseridos com sucesso\n"
              f"total de linhas: {linhas}\n"
              f"total de palavras: {total_palavras}\n"
              f"total de caracteres: {total_caracteres}.")
except FileNotFoundError:
    print("\nArquivo informado não encontrado!")
