"""
4) Faça um programa que receba do usuário um arquivo texto e mostre na tela quantas letras são vogais
   e quantas são consoantes
"""


import re
from collections import Counter


def vogais(string):
    """
    Conta quantas vogais há em uma string independentemente se maiúscula ou minúscula
    :param string: Qualquer string
    :return: quantidade de vogais
    """
    return Counter(re.sub('[^aeiouAEIOU]', '', string))


def consoantes(string):
    """
    Conta quantas consoantes há em uma string independentemente se maiúscula ou minúscula
    :param string: Qualquer string
    :return: quantidade de consoantes
    """
    return Counter(re.sub('[~^aeiouAEIOU]', '', string))


path = str(input("Informe o caminho do arquivo para saber quantas vogais e consoantes o arquivo possui: "))

try:
    with open(path, "r") as arquivo:
        texto = arquivo.readlines()
        linhas = len(texto)
        total_vogais = 0
        total_consoantes = 0
        for frase in texto:
            qtde_vogais = vogais(frase)
            total_vogais += sum([valor for valor in qtde_vogais.values()])
            qtde_consoantes = consoantes(frase)
            total_consoantes += sum([valor for valor in qtde_consoantes.values()])
        print(f"Em {path} há um total de {total_vogais} vogais e um total de {total_consoantes} consoantes.")
except FileNotFoundError:
    print("\nArquivo informado não encontrado!")
