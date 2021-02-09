"""
6) Faça um programa que receba do usuário um arquivo texto e mostre na tela quantas vezes cada letra do alfabeto
   aparece dentro do arquivo.
"""


from collections import Counter

print("Digite o caminho do arquivo para saber quantas vezes cada letra do alfabete aparece no arquivo selecionado.")
path = str(input("Informe o caminho do arquivo: "))

try:
    with open(path, "r") as arquivo:
        texto = arquivo.readlines()
        dicts = []
        for frase in texto:
            dicts.append(Counter(frase))
        total_caracteres = {k: sum(d[k] for d in dicts) for k in dicts[0]}
        print(f"Em {path} há a seguinte distribuição de caractere {total_caracteres}.")
except FileNotFoundError:
    print("\nArquivo informado não encontrado!")
