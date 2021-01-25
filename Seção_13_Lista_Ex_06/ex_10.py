"""
10) Faça um programa que receba o nome de um arquivo de entrada e outro de saída. O arquivo de entrada contém em cada
    linha o nome de uma cidade (ocupando 40 caracteres) e o seu número de habitantes. O programa deverá ler o arquivo de
    entrada e gerar um arquivo de saída onde aparece o nome da cidade mais populosa seguida pelo seu número de
    habitantes.
"""

print("Informe um arquivo de entrada e um arquivo de saída.")

path1 = str(input("Digite o caminho do arquivo de entrada: "))
path2 = str(input("Digite o caminho do arquivo de saída: "))

try:
    with open(path1, "r", encoding="utf-8") as arquivo1:
        with open(path2, "w", encoding="utf-8") as arquivo2:
            linhas = arquivo1.readlines()
            res_linha = {}
            # Um for em cada linha do texto
            for linha in linhas:
                # Usando o split(' ') na linha separamos as todos os espaços vazios,
                split_linha = linha.split(' ')
                # Usando o filter() com a função None eliminamos os elementos vazios sobrando uma lista com duas strings
                filtro_linha = list(filter(None, split_linha))
                # Como temos uma lista com duas str, adicionamos ao dicionario a chave = indice[0] e o valor = indice[1]
                res_linha[filtro_linha[0]] = int(filtro_linha[1])
            # Pegaremos a chave que contem o maior valor
            maior_cidade = max(res_linha, key=res_linha.get)
            # Salvando no novo aquivo a cidade que tem a maior população
            arquivo2.write(f"{maior_cidade}: {res_linha[maior_cidade]}")
    print("\nInformações inseridas no arquivo com sucesso!")
except FileNotFoundError:
    print("\nO arquivo informado não foi encontrado ou o programa não tem permissão para criar um diretório/pasta!")
except OSError:
    print("\nO SO não aceita caracteres especiais em nomes de arquivo!")
except ValueError:
    print("\nO modo que as informações se encontram no arquivo é inválido!")
except IndexError:
    print("\nO modo que as informações se encontram no arquivo é inválido!")
