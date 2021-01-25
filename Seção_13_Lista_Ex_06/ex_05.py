"""
5) Faça um programa que receba do usuário um arquivo texto e um caracter. Mostre na tela quantas vezes aquele
   caractere ocorre dentro do arquivo.
"""

from collections import Counter


def cont_caractere(string, caractere):
    """
    Conta quantas vezes um caractere aparece em uma string independentemente se maiúscula ou minúscula
    :param string: Qualquer string
    :param caractere: Caractere que se deseja contar
    :return: quantidade de vezes que o caractere aparece
    """
    caracteres = Counter(string)
    return int(caracteres[caractere])


print("Digite o caminho do arquivo e um caractere para saber quantas vezes o caractere aparece no arquivo selecionado.")
path = str(input("Informe o caminho do arquivo: "))
caractere = str(input("Informe o caractere para saber quantas vezes ele aparece no arquivo: "))

try:
    with open(path, "r") as arquivo:
        texto = arquivo.readlines()
        total = 0
        for frase in texto:
            qtde = cont_caractere(frase, caractere)
            total += qtde
        print(f"Em {path} o caractere {caractere} aparece {total} vezes.")
except FileNotFoundError:
    print("\nArquivo informado não encontrado!")
