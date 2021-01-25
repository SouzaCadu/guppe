"""
11) Faça um programa no qual o usuário informa o nome do arquivo e uma palavra, e retorne o número de vezes que aquela
    palavra aparece no arquivo.
"""

from collections import Counter


def cont_palavra(texto, palavra):
    """
    Conta quantas vezes uma palavra aparece em um texto extamente como o usuário informar
    :param texto: Qualquer texto
    :param palavra: Palavra que se deseja contar
    :return: quantidade de vezes que a palavra aparece no texto
    """
    palavras = Counter(texto)
    return int(palavras[palavra])


print("Digite o caminho do arquivo e uma palavra para saber quantas vezes a palavra aparece no arquivo selecionado\n"
      "com a correspondencia exata.")
path = str(input("Informe o caminho do arquivo: "))
palavra = str(input("Informe a palavra para saber quantas vezes ele aparece no arquivo: "))

try:
    with open(path, "r") as arquivo:
        texto = arquivo.readlines()
        total = 0
        for frase in texto:
            qtde = cont_palavra(frase.split(), palavra)
            total += qtde
        print(f"Em {path} a palavra {palavra} aparece {total} vezes.")
except FileNotFoundError:
    print("\nArquivo informado não encontrado!")
