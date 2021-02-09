"""
1) Escreva um programa que:
    (a) Crie/abra um arquivo texto de nome "arq.txt"
    (b) Permita que o usuário grave diversos caracteres nesse arquivo, até que o usuário
    entre com o caractere '0'
    (c) Feche o arquivo
Agora, abra e leia o arquivo, caarctere por caractere, escreva na tela todos os caracteres
armazenados
"""

try:
    with open("arq.txt", "w", encoding='utf-8') as arq:
        while True:
            caractere = str(input("Digite qualquer caractere ou zero '0' para sair: ")).strip()
            if caractere != "0":
                arq.write(f"{caractere}\n")
            else:
                break

except FileNotFoundError:
    print("\nO programa não possui permissão para criar um diretório/pasta!")

except OSError:
    print("\nO SO não aceita caracteres especiais em nomes de arquivo!")
